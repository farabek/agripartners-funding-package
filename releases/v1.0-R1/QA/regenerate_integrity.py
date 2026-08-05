import hashlib, json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()

payload={}
for path in sorted(p for p in root.rglob('*') if p.is_file()):
    rel=path.relative_to(root).as_posix()
    if rel not in {'MANIFEST.json','SHA256SUMS.txt'}: payload[rel]=digest(path)
manifest={
    'package':'AgriPartners Development Round Funding Package — Authoritative Master Edition',
    'edition':'1.0-R1',
    'publication_date':'2026-08-05',
    'status':'Publication Ready — Remediation Verified',
    'canonical_pdf_generator':'LibreOffice 25.8.7.3',
    'canonical_pdf_pages':186,
    'files':payload,
}
(root/'MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
lines=[]
for path in sorted(p for p in root.rglob('*') if p.is_file() and p.name!='SHA256SUMS.txt'):
    lines.append(f'{digest(path)}  {path.relative_to(root).as_posix()}')
(root/'SHA256SUMS.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')
print(f'manifest_payloads={len(payload)} checksums={len(lines)}')
