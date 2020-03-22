import turtle

def star(name, len):
    for i in range(5):
        name.forward(len)
        name.right(144)

screen = turtle.Screen()
casper = turtle.Turtle()

star(casper, 100)
screen.exitonclick()