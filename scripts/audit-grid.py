# Flags spacing/size values (px/rem) that break the grid: multiples of 8, or of 4 below 24px.
# Exempt: hairlines (<=1px), borders/outlines, opacity, percentages, unitless line-heights.
# Run from repo root: python3 scripts/audit-grid.py
import re,glob,sys
files=glob.glob('src/**/*.css',recursive=True)+glob.glob('src/**/*.astro',recursive=True)
skip_props=('letter-spacing','border','outline','opacity','--tracking','filter','z-index','font-weight','--ease','--dur','transition','stroke')
bad=[]
for f in files:
    for n,line in enumerate(open(f),1):
        l=line.strip()
        if l.startswith(('/*','//','<!--','*')): continue
        for m in re.finditer(r'(?<![\w.#-])(-?\d*\.?\d+)(rem|px)\b',l):
            ctx=l[:m.start()]
            if any(k in ctx.split(';')[-1] for k in skip_props): continue
            v=float(m.group(1)); px=v*16 if m.group(2)=='rem' else v
            a=abs(px)
            if a<=1: continue            # hairlines
            ok = (a%8==0) if a>=24 else (a%4==0)
            if not ok: bad.append((f,n,m.group(0),f'{px:g}px',l[:90]))
for b in bad: print(*b,sep=' | ')
print(len(bad),'non-compliant')
