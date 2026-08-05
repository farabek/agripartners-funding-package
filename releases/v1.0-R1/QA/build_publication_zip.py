from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

root=Path(__file__).resolve().parents[1]
output=root.parent/'AgriPartners_Development_Round_Funding_Package_AME_v1.0_R1_Publication.zip'
arcroot='AgriPartners_Development_Round_Funding_Package_AME_v1.0'
with ZipFile(output,'w',ZIP_DEFLATED,compresslevel=9) as z:
    for path in sorted(p for p in root.rglob('*') if p.is_file()):
        z.write(path,f'{arcroot}/{path.relative_to(root).as_posix()}')
print(output)
