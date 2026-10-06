"""Generates the watercolor-edge alpha masks in src/assets/photo-mask-*.webp (landscape/portrait/square).
Shape: a soft "squircle-oval" (superellipse, exponent N) fading irregularly into the paper, with the edge wander
capped so it never reaches the image border. Run from the repo root: python3 scripts/gen-photo-masks.py
Tweak N (ovalness: 2 = true ellipse, higher = squarer), WIDTH (fade), WOB (edge wander), BLOOM (bleed nibbles; 0 = off)."""
import numpy as np, cv2
from PIL import Image
N, WIDTH, WOB, BLOOM = 2.6, 0.17, 0.55, 0.0   # defaults (soft fade, used for art)
SOFT = dict(N=4.0, WIDTH=0.07, WOB=0.30)       # light feather for photos of people: keeps faces, still no hard edge
BLEND = dict(N=2.8, WIDTH=0.22, WOB=0.35, BLUR=0.04, inset=0.07)
MID = dict(N=3.6, WIDTH=0.12, WOB=0.30, BLUR=0.03, inset=0.03)   # between soft and blend: for a photo whose subject sits near a corner  # extra-soft, long feather: Our Story collages, so overlapping photos melt together
def smooth(x,a,b): t=np.clip((x-a)/(b-a),0,1); return t*t*(3-2*t)
def make(W,H,seed,name,inset=0.02,N=N,WIDTH=WIDTH,WOB=WOB,BLUR=0.012):
    def noise(s,sigma): r=np.random.default_rng(seed*100+s).standard_normal((H,W)).astype(np.float32); f=cv2.GaussianBlur(r,(0,0),sigma); return (f-f.mean())/f.std()
    yy,xx=np.mgrid[0:H,0:W].astype(np.float32); m=min(W,H)
    a_=(W-1)/2*(1-inset); b_=(H-1)/2*(1-inset)
    u=np.abs((xx-(W-1)/2)/a_); v=np.abs((yy-(H-1)/2)/b_)
    rho=(u**N+v**N)**(1.0/N)                                # superellipse radius: 1 on the boundary
    d=(1-rho)*min(a_,b_)                                    # approximate inward distance (px)
    disp=WOB*m*(0.7*noise(1,m*0.14)+0.3*noise(2,m*0.07))   # low-frequency only: broad, gentle wander (no fine nibbles)
    disp=0.03*m*np.tanh(disp/(0.03*m))                      # cap the wander
    w=m*WIDTH*(1.0+0.28*noise(4,m*0.12))                    # fade width varies around the edge
    a=smooth(d+disp,0,np.maximum(w,m*0.08))
    bloom=smooth(noise(5,m*0.05),1.1,2.1)*smooth(m*0.14-d,0,m*0.06)*BLOOM
    a=np.clip(a*(1-bloom),0,1)
    border=np.minimum(np.minimum(xx,W-1-xx),np.minimum(yy,H-1-yy)); a*=smooth(border,0,m*0.05)   # transparent at the border
    a=np.clip(cv2.GaussianBlur(a.astype(np.float32),(0,0),m*BLUR),0,1); a*=smooth(border,1,m*0.04)   # exactly 0 on the image border   # final blur: no hard spots anywhere
    Image.fromarray(np.dstack([np.full((H,W,3),255,np.uint8),(a*255).astype(np.uint8)]),'RGBA').save(f"src/assets/{name}.webp",quality=92,method=6)
make(720,480,1,'photo-mask-landscape'); make(480,720,2,'photo-mask-portrait'); make(560,560,3,'photo-mask-square')

make(720,480,1,'photo-mask-landscape-soft',inset=0.01,**SOFT); make(480,720,2,'photo-mask-portrait-soft',inset=0.01,**SOFT); make(560,560,3,'photo-mask-square-soft',inset=0.01,**SOFT)
make(720,480,1,'photo-mask-landscape-blend',**BLEND); make(480,720,2,'photo-mask-portrait-blend',**BLEND); make(560,560,3,'photo-mask-square-blend',**BLEND)
make(720,480,1,'photo-mask-landscape-mid',**MID); make(480,720,2,'photo-mask-portrait-mid',**MID); make(560,560,3,'photo-mask-square-mid',**MID)
