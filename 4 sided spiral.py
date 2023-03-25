# 4 SIDED SPIRAL
import turtle
pen=turtle.Pen()
turtle.bgcolor("black")
pen.speed(0)
colors=["red","yellow","blue","green"]
#for x in range(100):
for x in range(1500):
    pen.pencolor(colors[x % 4] )
    #pen.forward(2*x\x)
    pen.circle(x)
    pen.left(91)
