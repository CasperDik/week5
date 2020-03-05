import turtle

def draw_poly (t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.right(360/n)


screen = turtle.Screen()
casper = turtle.Turtle()

draw_poly(casper, 5, 50)

screen.exitonclick()