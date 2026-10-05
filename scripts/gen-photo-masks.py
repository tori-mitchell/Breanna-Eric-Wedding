"""Generates the watercolor-edge alpha masks in src/assets/photo-mask-*.webp (landscape/portrait/square).
Edge distance comes from a rounded rectangle (soft corners, no mitred points), inset from the border so the
irregular fade never runs into the image edge. Run from the repo root: python3 scripts/gen-photo-masks.py"""
import numpy as np, cv2
from PIL import Image
def smooth(x,a,b): t=np.clip((x-a)/(b-a),0,1); return t*t*(3-2*t)
def make(W,H,seed,name):
    def noise(s,sigma): r=np.random.default_rng(seed*100+s).standard_normal((H,W)).astype(np.float32); f=cv2.GaussianBlur(r,(0,0),sigma); return (f-f.mean())/f.std()
    yy,xx=np.mgrid[0:H,0:W].astype(np.float32); m=min(W,H)
    inset=0.025*m; R=0.15*m                                  # shape margin from the canvas edge; corner radius
    px,py=np.abs(xx-(W-1)/2),np.abs(yy-(H-1)/2)
    qx,qy=px-((W-1)/2-inset-R),py-((H-1)/2-inset-R)
    sdf=np.hypot(np.maximum(qx,0),np.maximum(qy,0))+np.minimum(np.maximum(qx,qy),0)-R
    d=-sdf                                                  # distance inside the rounded rectangle (px)
    disp=0.024*m*noise(1,m*0.10)+0.010*m*noise(2,m*0.035)+0.003*m*noise(3,m*0.01)   # wandering edge
    disp=0.02*m*np.tanh(disp/(0.02*m))                      # cap the wander so the edge can't reach the border
    width=m*0.085*(1.0+0.30*noise(4,m*0.12))                 # fade width varies side to side
    a=smooth(d+disp,0,np.maximum(width,m*0.04))**1.15
    bloom=smooth(noise(5,m*0.05),1.1,2.1)*smooth(m*0.12-d,0,m*0.05)*0.30
    a=np.clip(a*(1-bloom),0,1)
    border=np.minimum(np.minimum(xx,W-1-xx),np.minimum(yy,H-1-yy))
    a*=smooth(border,0,m*0.02)                              # guarantee transparency at the image border
    a=np.clip(a+0.010*np.random.default_rng(seed).standard_normal((H,W))*(a>0.02)*(a<0.98),0,1)
    Image.fromarray(np.dstack([np.full((H,W,3),255,np.uint8),(a*255).astype(np.uint8)]),'RGBA').save(f"src/assets/{name}.webp",quality=92,method=6)
make(720,480,1,'photo-mask-landscape'); make(480,720,2,'photo-mask-portrait'); make(560,560,3,'photo-mask-square')
