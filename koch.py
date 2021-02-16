import turtle as t
import colorsys as cs
import math as m
import sys

def koch(depth,size,orientation=1):
    if depth==0:
        t.forward(size)
        return
    size/=3
    depth-=1
    koch(depth,size,orientation)
    t.left(60*orientation)
    koch(depth,size,orientation)
    t.left(-120*orientation)
    koch(depth,size,orientation)
    t.left(60*orientation)
    koch(depth,size,orientation)

def snowflake(depth,size,rotation=0):
    t.penup()
    if rotation==1:
        t.setpos(size*(3**(1/2)/3),0)
        t.right(90)
    else:
        t.setpos(0,size*(3**(1/2)/3))
        
    t.right(60)
    t.pendown()
    for _ in range(3):
        koch(depth,size,1)
        t.right(120)
    t.penup()
    t.setpos(0,0)
    t.left(60)

    if rotation==1:
        t.left(90)
        
    t.pendown()
        
####################

if len(sys.argv)>=3:
    depth = int(sys.argv[1])
    size = int(sys.argv[2])
else:
    depth = 6
    size = 100

t.speed(0)
f = (5/4)**(3/2)
t.bgcolor("#000")
for d in range(1,depth):
    t.pensize(2*(depth-d)-1)
    t.pencolor(cs.hsv_to_rgb(((d*0.6)%1)*0.2+0.5,0.8,1))
    snowflake(d,size*f**(d),(-1)**d)
input()
