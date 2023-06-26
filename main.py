import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

screen = t.Screen()

colors = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen"
]


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def spyro(a):  # set color mode to accept RGB values in range 0-1
    n = 10
    for _ in range(int(360 / a)):
        timmy.speed("fastest")
        timmy.color(rand_color())
        timmy.circle(-100)
        timmy.right(n)


spyro(4)

screen.exitonclick()

