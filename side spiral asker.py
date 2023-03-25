#side spiral asker
import turtle
pen=turtle.Pen()
turtle.bgcolor("black")
pen.speed(0)
sides=int(input("please enter the number of sides for your spiral: "))
colorsCsv=input("please enter comma separated colors which are equal to the number of sides: ")
#colorsCsv=green,blue,yellow,red
colors=colorsCsv.split(",")
for x in range(360):
  pen.pencolor(colors[x%sides])
  pen.forward(x * 3/sides + x)
  pen.left(360/sides + 1)
  pen.width(x*sides/100)
