import argparse
from pathlib import Path
from PIL import Image, ImageDraw

ap=argparse.ArgumentParser(); ap.add_argument('source'); ap.add_argument('output')
args=ap.parse_args(); src=Path(args.source); dst=Path(args.output); dst.mkdir(parents=True,exist_ok=True)
files=sorted(src.glob('page-*.png'),key=lambda p:int(p.stem.split('-')[-1]))
cols=4; rows=4; thumb_w=382
for batch in range(0,len(files),cols*rows):
    opened=[]
    for p in files[batch:batch+cols*rows]:
        im=Image.open(p).convert('RGB'); h=round(im.height*thumb_w/im.width)
        opened.append((p,im.resize((thumb_w,h))))
    cell_h=max(im.height for _,im in opened)+28
    sheet=Image.new('RGB',(cols*thumb_w,rows*cell_h),'#777777'); d=ImageDraw.Draw(sheet)
    for i,(p,im) in enumerate(opened):
        x=(i%cols)*thumb_w; y=(i//cols)*cell_h+22; sheet.paste(im,(x,y)); d.text((x+4,y-19),p.stem,fill='white')
    first=batch+1; last=batch+len(opened); sheet.save(dst/f'pages-{first:03d}-{last:03d}.jpg',quality=90)
print(len(files))
