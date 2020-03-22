import turtle

def pattern(name, n, size):
    for i in range(3):
        name.forward(size)
        name.right(90)
    name.forward(size)
    name.right(90 + (360 / n))

screen = turtle.Screen()
casper = turtle.Turtle()
n = 20

for i in range(n):
    pattern(casper, n, 100)



screen.exitonclick()