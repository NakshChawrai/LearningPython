#6 sided spiral
import turtle
pen=turtle.Pen()
turtle.bgcolor("black")
pen.speed(0)
sides = 6
colors=["red","yellow","blue","orange","green","purple"]
for x in range(360):
  pen.pencolor(colors[x%sides])
  pen.forward(x * 3/sides + x)
  pen.left(360/sides + 1)
  pen.width(x*sides/100)
