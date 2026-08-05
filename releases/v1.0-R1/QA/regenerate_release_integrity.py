#!/usr/bin/env python3
"""Generate the release-payload manifest and SHA-256 checksum list."""

from datetime import date
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_DIR = ROOT / "Manifest"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest().upper()


def payload_files():
    for path in sorted(ROOT.rglob("*"), key=lambda p: p.relative_to(ROOT).as_posix().lower()):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if rel.parts[0] == "Manifest":
            continue
        if rel.parts[0] == "Archive" and path.name != "README.md":
            continue
        if "__pycache__" in rel.parts:
            continue
        yield path


def main() -> None:
    MANIFEST_DIR.mkdir(exist_ok=True)
    files = []
    lines = []
    for path in payload_files():
        rel = path.relative_to(ROOT).as_posix()
        value = digest(path)
        files.append({"path": rel, "bytes": path.stat().st_size, "sha256": value})
        lines.append(f"{value}  {rel}")
    manifest = {
        "publication": "AgriPartners Development Round Funding Package",
        "edition": "Authoritative Master Edition",
        "version": "v1.0 R1",
        "release_status": "Release Authorized",
        "manifest_scope": "release payload; excludes generated archive-control artifacts and Manifest directory to avoid circular hashes",
        "generated": str(date(2026, 8, 5)),
        "file_count": len(files),
        "files": files,
    }
    (MANIFEST_DIR / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (MANIFEST_DIR / "SHA256SUMS.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"payload_files={len(files)}")


if __name__ == "__main__":
    main()
