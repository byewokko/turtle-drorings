import turtle as t
import colorsys as cs
import math as m
import sys
from time import sleep

class Curve():
    def __init__(self,depth,size,speed=0):
        self.counter = 0
        self.depthmax = depth
        self.size = size
        t.speed(0)
        t.penup()
        t.setpos(-size/2,-size/2)
        t.pendown()
        t.speed(speed)
        t.bgcolor("#000000")

    def hil(self):
        margin = self.size/2**(2+self.depthmax)
        
        t.pensize(1)
        t.pencolor("#FFF")
        
        t.pendown()
        self.frame(self.size)
        t.penup()
        
        t.forward(margin)
        t.left(90)
        t.forward(margin)
        
        t.pensize(1)
        t.pendown()
        self.hilbert(self.size/2,self.depthmax)
        self.counter *=1.52
        t.pensize(3)
        self.hilbert(self.size*4,self.depthmax)
        t.penup()

        #t.setpos(0,0)
        t.pencolor("#FFF")

    def frame(self, size):
        for _ in range(4):
            t.forward(size)
            t.left(90)
        
    def hilbert(self,size,depth=0,orient=1):

        
        if depth<=0:
            t.pencolor(cs.hsv_to_rgb((0.6+self.counter/(4**self.depthmax))%1,1,1))
            #t.fillcolor(cs.hsv_to_rgb((0.1+self.counter/(4**self.depthmax))%1,1,1))
            if self.counter > 4**self.depthmax*93/100 and self.counter < 4**self.depthmax:
                self.counter *=2
                
                
            self.counter += 1
            #t.begin_fill()
            ##
            #t.penup()
            t.forward(size)
            t.right(orient*90)
            ##
            
            t.forward(size)
            #t.end_fill()
            ##
            t.right(orient*90)
            t.forward(size)
            #t.pendown()
            t.left((self.counter/(4**self.depthmax*9/10))**(5)*m.sin(m.pi*self.counter*0.03))
            return

        size = size/2
        depth -= 1
        
        t.right(orient*90)
        self.hilbert(size,depth,-orient)
        t.right(orient*90)

        self.link(size,depth,orient)

        self.hilbert(size,depth,orient)
        t.right(-orient*90)

        self.link(size,depth,orient)

        t.right(-orient*90)
        self.hilbert(size,depth,orient)

        self.link(size,depth,orient)

        t.right(orient*90)
        self.hilbert(size,depth,-orient)
        t.right(orient*90)


    def link(self,size,depth=1,orient=1):
        t.forward(size/2**depth)
    

if len(sys.argv)>=3:
    depth = int(sys.argv[1])
    size = int(sys.argv[2])
else:
    depth = 4
    size = 400
    
c = Curve(depth,size)
c.hil()

sleep(1)
input()
