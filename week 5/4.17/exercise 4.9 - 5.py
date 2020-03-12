import turtle

def spiral1(name, size, n):
    for i in range(n):
        name.forward(size*(i+1))
        name.right(90)

def spiral2(name, size, n):
    for i in range(n):
        name.forward(size*(i+1))
        name.right(90+(360/n))

screen = turtle.Screen()
casper = turtle.Turtle()
casper.speed(10)
spiral1(casper,2,100)
spiral2(casper,2,100)
screen.exitonclick()