import turtle
import math

screen = turtle.Screen()
casper = turtle.Turtle()
casper.speed(10)


x = 10 # base length sides


for i in range(15):
    angle = 360/(i+3)
    sides = i + 3
    int(sides)
    int(angle)
    if i == 0:
        X = x / 2
        y = (math.sqrt((x ** 2) - ((x / 2) ** 2))) / 2
        casper.penup()
        casper.setposition(-X, y)
        casper.pendown()
        for j in range(sides):
            casper.forward(x)
            casper.right(angle)
    else:
        a = (x * (i + 1)) / (2 * math.tan(((180 / sides)) * 3.14159 / 180))
        casper.penup()
        casper.setposition(0, 0)
        casper.left(90)
        casper.forward(a)
        casper.left(90)
        casper.forward((x*(i+1))/2)
        casper.left(180)
        casper.pendown()
        for g in range(sides):
            casper.forward(x * (i + 1))
            casper.right(angle)


screen.exitonclick()