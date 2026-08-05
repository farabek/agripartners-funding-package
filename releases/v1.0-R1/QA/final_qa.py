import hashlib, json, re, sys, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

root=Path(__file__).resolve().parents[1]; failures=[]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def check(ok,msg):
    print(('PASS ' if ok else 'FAIL ')+msg)
    if not ok: failures.append(msg)

sections=sorted((root/'Sections').glob('*.md')); appendices=sorted((root/'Appendices').glob('*.md'))
check(len(sections)==21 and [int(p.name[:2]) for p in sections]==list(range(1,22)),'section completeness')
check(len(appendices)==10 and [p.name[0] for p in appendices]==list('ABCDEFGHIJ'),'appendix completeness')
master=(root/'Master/AgriPartners_Development_Round_Funding_Package_AME_v1.0.md').read_text(encoding='utf-8')
check(all(p.read_text(encoding='utf-8').strip() in master for p in sections),'canonical Section bodies occur exactly in Master Markdown')
check(all(p.read_text(encoding='utf-8').strip() in master for p in appendices),'canonical Appendix bodies occur exactly in Master Markdown')
c=(root/'Appendices/C_Deliverable_Milestone_Crosswalk.md').read_text(encoding='utf-8')
titles=['Expense Platform Complete','Operator Workspace Complete','Evidence Layer Complete','Investor Transparency Complete','Beta Candidate Complete']
check(all(f'Milestone {i} — {t}' in c for i,t in enumerate(titles,1)) and not re.search(r'\bM6\b|Milestone 6',c),'Appendix C matches five Section 13 milestones')
allmd='\n'.join(p.read_text(encoding='utf-8') for p in root.rglob('*.md') if 'QA' not in p.relative_to(root).parts)
check(not re.search(r'\b(?:TODO|TBD)\b|\[INSERT[^]]*\]|\{\{[^}]+\}\}',allmd,re.I),'no TODO/TBD/placeholders')
refs={int(x) for x in re.findall(r'\bSections?\s+(\d+)\b',allmd)}
check(all(1<=x<=21 for x in refs),'Section cross-reference range')
apps=set(re.findall(r'\bAppendix\s+([A-Z])\b',allmd))
check(all(x in 'ABCDEFGHIJ' for x in apps),'Appendix cross-reference range')

manifest=json.loads((root/'MANIFEST.json').read_text(encoding='utf-8'))['files']
check(all((root/n).is_file() and sha(root/n)==h for n,h in manifest.items()),'Manifest integrity')
sums={line.split('  ',1)[1]:line.split('  ',1)[0] for line in (root/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines() if line}
check(all((root/n).is_file() and sha(root/n)==h for n,h in sums.items()),'SHA256SUMS integrity')
check(set(sums)=={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name!='SHA256SUMS.txt'},'SHA256SUMS coverage')

docx=root/'Master/AgriPartners_Development_Round_Funding_Package_AME_v1.0.docx'; W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; ns={'w':W}
with zipfile.ZipFile(docx) as z: xml=ET.fromstring(z.read('word/document.xml'))
tables=xml.findall('.//w:tbl',ns); geometry=True
for t in tables:
    tw=t.find('./w:tblPr/w:tblW',ns); grid=[int(x.get(f'{{{W}}}w')) for x in t.findall('./w:tblGrid/w:gridCol',ns)]
    geometry &= tw is not None and tw.get(f'{{{W}}}type')=='dxa' and int(tw.get(f'{{{W}}}w'))==sum(grid)
    for row in t.findall('w:tr',ns):
        geometry &= len(row.findall('w:tc',ns))==len(grid)
        for i,tc in enumerate(row.findall('w:tc',ns)):
            cw=tc.find('w:tcPr/w:tcW',ns); geometry &= cw is not None and cw.get(f'{{{W}}}type')=='dxa' and int(cw.get(f'{{{W}}}w'))==grid[i]
check(len(tables)==9 and geometry,'DOCX deterministic table geometry')
check(not failures,'overall structural QA')
sys.exit(1 if failures else 0)
