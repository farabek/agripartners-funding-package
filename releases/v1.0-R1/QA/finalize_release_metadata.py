#!/usr/bin/env python3
"""Apply the approved v1.0 R1 cover and package metadata to the Master DOCX."""

from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "Master" / "AgriPartners_Development_Round_Funding_Package_AME_v1.0.docx"
OLD = "Authoritative Master Edition 1.0"
NEW = "Authoritative Master Edition — Version v1.0 R1"
CP = "http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
DC = "http://purl.org/dc/elements/1.1/"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def update_document_xml(data: bytes) -> bytes:
    root = ET.fromstring(data)
    matches = 0
    for paragraph in root.iter(f"{{{W}}}p"):
        nodes = list(paragraph.iter(f"{{{W}}}t"))
        if "".join(node.text or "" for node in nodes) == OLD:
            nodes[0].text = NEW
            for node in nodes[1:]:
                node.text = ""
            matches += 1
    if matches != 1:
        raise RuntimeError(f"Expected one exact cover label; found {matches}")
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def update_core_xml(data: bytes) -> bytes:
    root = ET.fromstring(data)
    values = {
        f"{{{DC}}}title": "AgriPartners Development Round Funding Package",
        f"{{{DC}}}subject": "Authoritative Master Edition — Version v1.0 R1",
        f"{{{CP}}}keywords": "AgriPartners; funding package; AME; v1.0 R1",
    }
    for tag, value in values.items():
        node = root.find(tag)
        if node is None:
            node = ET.SubElement(root, tag)
        node.text = value
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def main() -> None:
    with ZipFile(DOCX, "r") as source, NamedTemporaryFile(
        suffix=".docx", delete=False, dir=DOCX.parent
    ) as tmp:
        temp_path = Path(tmp.name)
        with ZipFile(tmp, "w", ZIP_DEFLATED) as target:
            for item in source.infolist():
                data = source.read(item.filename)
                if item.filename == "word/document.xml":
                    data = update_document_xml(data)
                elif item.filename == "docProps/core.xml":
                    data = update_core_xml(data)
                target.writestr(item, data)
    temp_path.replace(DOCX)
    print(DOCX)


if __name__ == "__main__":
    main()
