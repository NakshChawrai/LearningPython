# SIDED SPIRAL
import turtle
pen=turtle.Pen()
pen.color("red,yellow, blue,green")
pen.speed(200)
#for x in range(100):
for x in range(1500):
    pen.pencolor(colors[x % 4] )
    pen.forward(x)
    pen.left(91)
