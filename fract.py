import turtle as t
from time import sleep
import colorsys as cs
import math as m

class Curve():
    counter = 0
    @classmethod
    def fract(self,depth,size,orient=1):
        if depth == 0:
            self.counter += 0.7
            t.fillcolor(cs.hsv_to_rgb(
                ((-m.sin(self.counter/160)+
                  m.cos(self.counter/120)/2+
                  m.sin(self.counter/30)/3
                )/16+1+0.09)%1,
                (m.sin(self.counter/110)+1)/8+0.75,
                (m.cos(self.counter/220)+1)/7+0.6
            ))
            t.forward(size)
            return

        #orient=1
        t.left(-30*orient)
        if depth == 1:
            t.begin_fill()
        self.fract(depth-1, size*3**(1/2)/3, -orient)
        t.left(120*orient)
        self.fract(depth-1, size*3**(1/2)/3, orient)
        if depth == 1:
            t.end_fill()
        t.left(-120*orient)
        self.fract(depth-1, size*3**(1/2)/3, -orient)
        t.left(30*orient)


depth = 7
size = 900
t.bgcolor("#000")
t.pencolor("#000")
t.penup()
t.speed(0)
t.setpos(-size/2,0)
t.pendown()
Curve.fract(depth,size,1)
input()
