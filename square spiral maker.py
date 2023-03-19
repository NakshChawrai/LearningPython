#square spiral maker.py
import turtle
pen=turtle.Pen()
penSpeed=input("please enter the speed of the pen: ")
pen.speed(float(penSpeed))
imageRange =input(" please enter a range of your choice: ")
penLeft=input("please enter the left value: ")
#for x in range(100):
for x in range(int(imageRange)):
    pen.forward(x)
    pen.left(int(penLeft))
    
