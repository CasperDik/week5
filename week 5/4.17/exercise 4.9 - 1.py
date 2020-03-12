import turtle

def square(casper, size):
    for i in range(4):
        casper.forward(size)
        casper.right(90)

screen = turtle.Screen()
casper = turtle.Turtle()
size = 10
for i in range(5):
    square(casper, size)
    casper.penup()
    casper.forward(2*size)
    casper.pendown()

screen.exitonclick()