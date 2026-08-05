#!/usr/bin/env python3
"""Build and describe the deterministic v1.0 R1 immutable ZIP archive."""

from hashlib import sha256
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_DIR = ROOT / "Archive"
ZIP_NAME = "AgriPartners_Development_Round_Funding_Package_AME_v1.0_R1_Immutable.zip"
ZIP_PATH = ARCHIVE_DIR / ZIP_NAME
SIDECAR = ARCHIVE_DIR / f"{ZIP_NAME}.sha256"
ARCHIVE_MANIFEST = ARCHIVE_DIR / "ARCHIVE_MANIFEST_v1.0_R1.json"
TOP = "agripartners-funding-package-v1.0-R1"


def digest_bytes(data: bytes) -> str:
    return sha256(data).hexdigest().upper()


def included_files():
    excluded = {ZIP_PATH.resolve(), SIDECAR.resolve(), ARCHIVE_MANIFEST.resolve()}
    for path in sorted(ROOT.rglob("*"), key=lambda p: p.relative_to(ROOT).as_posix().lower()):
        if path.is_file() and path.resolve() not in excluded and "__pycache__" not in path.parts:
            yield path


def main() -> None:
    ARCHIVE_DIR.mkdir(exist_ok=True)
    entries = []
    with ZipFile(ZIP_PATH, "w", ZIP_DEFLATED, compresslevel=9) as archive:
        for path in included_files():
            rel = path.relative_to(ROOT).as_posix()
            data = path.read_bytes()
            info = ZipInfo(f"{TOP}/{rel}", date_time=(2026, 8, 5, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data, compresslevel=9)
            entries.append({"path": rel, "bytes": len(data), "sha256": digest_bytes(data)})
    zip_hash = digest_bytes(ZIP_PATH.read_bytes())
    SIDECAR.write_text(f"{zip_hash}  {ZIP_NAME}\n", encoding="ascii")
    archive_manifest = {
        "publication": "AgriPartners Development Round Funding Package",
        "edition": "Authoritative Master Edition",
        "version": "v1.0 R1",
        "archive": ZIP_NAME,
        "archive_sha256": zip_hash,
        "top_level_directory": TOP,
        "entry_count": len(entries),
        "entries": entries,
    }
    ARCHIVE_MANIFEST.write_text(
        json.dumps(archive_manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    with ZipFile(ZIP_PATH) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("ZIP CRC validation failed")
    print(f"entries={len(entries)}")
    print(f"sha256={zip_hash}")


if __name__ == "__main__":
    main()
