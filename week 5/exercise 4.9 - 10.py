import turtle

def star(name, len):
    for j in range(5):
        for i in range(5):
            name.forward(len)
            name.right(144)
        name.penup()
        name.forward(350)
        name.right(144)
        name.pendown()

screen = turtle.Screen()
casper = turtle.Turtle()

star(casper, 100)
screen.exitonclick()