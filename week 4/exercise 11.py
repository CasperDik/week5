
import turtle
screen = turtle.Screen()
casper = turtle.Turtle()


list = [(0, 100), (90, 100), (135, 141.42), (-135,100), (-90,100), (135,70.71), (90, 70.71), (90, 141.42)]
casper.speed(2)

for left, forward in list:
    casper.left(left)
    casper.forward(forward)

screen.exitonclick()
