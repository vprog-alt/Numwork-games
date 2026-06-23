from bprg import *
from new_font import *

bg,c,c2=(0,0,0),(255,186,42),(255,255,255)

end=False

def charge(txt,v,nb):
  background(bg),penup(),goto(0,27),color(c),pendown(),draw(txt,160-5*len(txt),115,c2,bg)
  for _ in range(nb):speed(v),goto(0,27),color(c),pensize(5),circle(-13),goto(0,27),color(bg),pensize(7),circle(-13),sleep(abs(v-10)/10)

def download(txt,v):
  background(bg),rect(50,100,220,8,c),rect(51,101,218,6,bg),draw(txt,160-5*len(txt),115,c2,bg)
  s=0
  while s<220:
    if randint(0,20-v)==0:s+=randint(1,2)
    rect(50,100,s,8,c),sleep(abs(v-10)/750)
  sleep(0.1)
  
def fini(txt):background(bg),draw(txt,160-5*len(txt),115,c2,bg),speed(10),penup(),pensize(6),goto(-14,16),color(0,220,20),pendown(),goto(0,2),goto(16,26),pensize(5),sleep(1)
def fail(txt):background(bg),draw(txt,160-5*len(txt),115,c2,bg),speed(10),penup(),pensize(6),goto(-13,26),color(255,0,0),pendown(),goto(12,2),penup(),goto(12,26),pendown(),goto(-13,2),pensize(5),sleep(1)

def animation(v1,v2,v3):
  hideturtle(),penup(),goto(0,27),color(c),pensize(5),pendown()
  charge("connection",v1,randint(1,7)),sleep(0.2)
  charge("waiting",v2,randint(1,4)),sleep(0.2)
  charge("finalisation",10,randint(4,6))
  download("download",v3)
  if randint(1,5)!=1:
    fini("downloaded!"),charge("finalisation",10,randint(5,7))
    end=True
  else:
    background((255,255,255))
    fail("fail to download"),sleep(2),background(bg),sleep(1.2)
    charge("reconnection",v1-1,randint(1,4)),sleep(0.3)
    charge("waiting",v1-1,randint(1,3)),sleep(0.3)
