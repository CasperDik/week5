import turtle

screen = turtle.Screen()
casper = turtle.Turtle()
casper.speed(10)

x = 10 # base length sides

for i in range(5):
    angle = 360/(i+3)
    sides = i + 3
    int(sides)
    int(angle)
    if sides == 3:
        for j in range(sides):
            casper.forward(x)
            casper.right(angle)
    else:
        casper.penup()
        casper.forward((x*i)/2)
        casper.left(90)
        casper.forward((x*i)/2)
        casper.left(90)
        casper.forward((x*(i+1))/2)
        casper.right(180)
        casper.pendown()
        for g in range(sides):
            casper.forward(x*(i+1))
            casper.right(angle)









screen.exitonclick()
