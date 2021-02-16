import turtle as t
import math as m
import colorsys as cs

t.speed(0)
t.bgcolor("#000000")
t.pencolor("#ff0000")

def fun1():
    t.pensize(2)
    x=0
    t.penup()
    #t.setpos(-200,-200)
    t.pendown()
    while True:
        x+=1
        t.pensize(7*(m.sin(m.pi*x*0.02)+1))
        t.pencolor(cs.hsv_to_rgb((2000+x*(1+0.1*m.sin(x*0.1)))/4000%1,
                                 1-(m.sin(m.pi*x*0.04)+1)/5,
                                 (m.sin(m.pi*x*0.02)+1)/2))
        t.forward(3+0.01*(x*(1+0.1*m.sin(x*0.1))))
        t.left(45*abs(m.cos(m.pi*x*0.01)))
        t.left(1)

def fun2():
    x=0
    t.penup()
    #t.setpos(-200,0)
    t.pendown()
    while True:
        x+=0.02
        y = (m.sin(m.pi*x*1) + m.sin(m.pi*x*2)/2 + m.sin(m.pi*x*4)/4 + m.sin(m.pi*x*8)/8)/2
        
        #t.pensize(7*(1.01+m.sin(m.pi*x*2)))
        t.pensize(12*((x-0.5)%1))
        t.pencolor(cs.hsv_to_rgb((0.2*m.sin(m.pi*x*1)-0.3+x/100)%1,
                                 (0.35*m.sin(m.pi*x*3/2)+0.5)%1,
                                 (x-0.5)%1))
        t.left(-20*y+2)
        t.forward(m.log(x+1))

fun2()
