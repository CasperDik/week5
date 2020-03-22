import turtle


def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.right(360 / n)

def draw_equitrangle(t, sz):
    n = 3
    draw_poly(t ,n, sz)



screen = turtle.Screen()
casper = turtle.Turtle()
casper.speed(10)

draw_equitrangle(casper,10)
screen.exitonclick()