from bprg import *

t,c,bg=8,(0,0,0),(255,255,255)
w=320//t
h=222//t+1

cells=[[0 for _ in range(w)]for _ in range(h)]
stepup=[row[:] for row in cells]
forward=[row[:] for row in cells]

def randcell(R):
  global cells
  for i in range(R):cells[randint(0,h-1)][randint(0,w-1)]=1  

lib=[[(0,0),(2,0),(1,1),(2,1),(1,2)],[(0,0),(0,1),(1,0),(1,1)],[(0,0),(1,0),(0,1),(2,1),(2,2),(0,3),(2,3),(0,4),(1,4)],[],[]]
detect=[(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

def affmap():
  global cells,forward,ed
  for y in range(h):
    for x in range(w):
      if ed or cells[y][x]!=forward[y][x]:
        rect(x*t,y*t,t,t,c if cells[y][x] else bg)
        
def step():
  global cells,stepup,forward
  stepup=[row[:] for row in cells]
  forward=[row[:] for row in cells]
  for y in range(h):
    for x in range(w):
      s=0
      for j,i in detect:
        ny,nx=y+j,x+i
        if 0<=ny<h and 0<=nx<w and cells[ny][nx]:s+=1
      stepup[y][x]=s in (2,3) if cells[y][x] else s==3
  cells=[row[:] for row in stepup]
  affmap()

def edit():
  global cells,ed,xc,yc
  affmap()
  ed=True
  while not key(52):
    xc,yc=passlimits(xc+(key(3)-key(0)),0,w-1),passlimits(yc+(key(2)-key(1)),0,h-1)
    if key(4):cells[yc][xc]=1
    elif key(17):cells[yc][xc]=0
    elif key(26) or key(27):
      cells=stepup=forward=[[0 for _ in range(w)]for _ in range(h)]
      if key(27):randcell(500)
      background(bg)
    for k in (12,13,14,15,16):
      if key(k):
        for x,y in lib[k-12]:cells[yc+y][xc+x]=True
    for k in (0,1,2,3,4,12,13,14,15,16,17,26,27):#aff
      if key(k):
        rect(xc*t,yc*t,t,t,bg)
        affmap()
        rect(xc*t,yc*t,t,t,(150,150,150) if cells[yc][xc] else (0,150,255))
    sleep(0.05)
  ed=False
  background(bg)
  affmap()

m=monotonic()+20

xc=yc=0
ed=False
background(bg)
randcell(700)
affmap()

while True:
  step()
  if key(52):
    release(52)
    affmap()
    edit()
    release(52)
