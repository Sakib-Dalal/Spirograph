import turtle as t
import random

my_turtle = t.Turtle()
my_screen = t.Screen()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        my_turtle.color(random_color())
        my_turtle.speed(10)
        my_turtle.left(size_of_gap)
        my_turtle.circle(100)


draw_spirograph(5)
my_screen.exitonclick()
