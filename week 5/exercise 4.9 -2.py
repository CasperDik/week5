import turtle

def square(casper, size):
    for i in range(4):
        casper.forward(size)
        casper.right(90)

screen = turtle.Screen()
casper = turtle.Turtle()
size = 10
center = 10
x = 0
y = 0
for i in range(5):
    casper.setposition(x + center, y + center)
    square(casper, size)
    size = size * 2
    center = center *2


screen.exitonclick()