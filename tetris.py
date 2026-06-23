from kandinsky import fill_rect as f, draw_string as d
from ion import *
from time import monotonic
from random import randrange
st=(
# o piece
[[(0,0),(1,0),(0,1),(1,1)]],
# s piece
(((1,0),(2,0),(0,1),(1,1)),((1,-1),(1,0),(2,0),(2,1))),
# z piece
(((0,0),(1,0),(1,1),(2,1)),((2,-1),(2,0),(1,0),(1,1))),
# i piece
(((0,0),(1,0),(2,0),(3,0)),((1,-1),(1,0),(1,1),(1,2))),
# j piece
(((0,0),(1,0),(2,0),(2,1)),((1,-1),(1,0),(1,1),(0,1)),((0,-1),(0,0),(1,0),(2,0)),((1,-1),(2,-1),(1,0),(1,1))),
# l piece
(((0,1),(0,0),(1,0),(2,0)),((0,-1),(1,-1),(1,0),(1,1)),((2,-1),(2,0),(1,0),(0,0)),((1,-1),(1,0),(1,1),(2,1))),
# t piece
(((1,0),(0,1),(1,1),(2,1)),((1,0),(1,1),(2,1),(1,2)),((0,1),(1,1),(2,1),(1,2)),((1,0),(0,1),(1,1),(1,2))))
def draw(x,y,idt,stat,col):
  for c in st[idt][stat%len(st[idt])]:
    f(x+c[0]*11,y+c[1]*11,10,10,col)
def collide(coo,idt,state):
  for c in st[idt][state%len(st[idt])]:
    if 10>coo[0]+c[0]>-1 and 20>coo[1]-c[1]>-1:
      if grid[coo[1]-c[1]][coo[0]+c[0]]!=-1:
        return 1
    else:
      return 1
  return 0
def transf(x,y,r):
  global coo,state
  if not collide((x,y),id,state):
    draw(55+coo[0]*11,210-coo[1]*11,id,state,COLORS[8])
    coo=[x,y]
    state=(state+r)%len(st[id])
    draw(55+x*11,210-y*11,id,state,COLORS[id])
    return 1
COLORS=(
(180,154,50),# o piece
(130,178,49),# s piece
(179,51,58),# z piece
(50,179,131),# i piece
(81,63,166),# j piece
(181,100,51),# l piece
(166,63,156),# t piece
(31,32,33),# background
(9,9,9), # game background
(194,224,255))# text 
t=[monotonic(),monotonic()]
grid=[[-1 for _ in range(10)]for _ in range(20)]
key_pressing={"KEY_ALPHA":0,"KEY_TOOLBOX":0,"KEY_BACKSPACE":0,"KEY_SHIFT":0}
key_pressed={k:0 for k in key_pressing}

f(0,0,320,222,COLORS[7])
d("L&R:",230,30,COLORS[9],COLORS[7])
d("Move",230,46,COLORS[9],COLORS[7])
d("Down:",230,66,COLORS[9],COLORS[7])
d("Fall",230,82,COLORS[9],COLORS[7])
d("Shift:",230,102,COLORS[9],COLORS[7])
d("Hold",230,118,COLORS[9],COLORS[7])
d("Alpha:",230,138,COLORS[9],COLORS[7])
d("Pause",230,154,COLORS[9],COLORS[7])
d("TBX&DEL:",230,174,COLORS[9],COLORS[7])
d("Rotate",230,192,COLORS[9],COLORS[7])
f(0,0,54,32,COLORS[9])
f(2,2,50,28,COLORS[7])
stock=[randrange(7) for _ in range(6)]
score=0
for x in range(10):
  for y in range(20):
    f(55+x*11,1+y*11,10,10,COLORS[8])
pause=0
id=-1
hold=randrange(7)
draw(5,5,hold,0,COLORS[hold])
run=1
while run:
  for k in key_pressing:
    key_pressed[k]=0
    if keydown(globals()[k]):
      if not key_pressing[k]:
        key_pressed[k]=1
      key_pressing[k]=1
    else:
      key_pressing[k]=0
  if key_pressed["KEY_ALPHA"]:
    pause=not pause
  if not pause:
    if id==-1:
      coo=[3,19]
      id=stock[0]
      stock.pop(0)
      stock.append(randrange(7))
      state=0
      locked=0
      if not collide(coo,id,state):
        draw(55+coo[0]*11,210-coo[1]*11,id,state,COLORS[id])
        f(180,5,50,182,COLORS[7])
        for y in range(6):
          draw(180,5+y*30,stock[y],0,COLORS[stock[y]])
        d(str(score),230,0,COLORS[9],COLORS[7])
      else:
        d("YOU LOST",70,101,COLORS[9],COLORS[7])
        run=0
    elif monotonic()-t[0]>0.25 or (keydown(KEY_DOWN) and monotonic()-t[0]>0.035):
      t[0]=monotonic()
      if not collide((coo[0],coo[1]-1),id,state):
        transf(coo[0],coo[1]-1,0)
      else:
        score+=2
