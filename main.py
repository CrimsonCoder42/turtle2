from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

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


def right_forward():
    timmy.right(90)
    timmy.forward(25)

def left_forward():
    timmy.left(90)
    timmy.forward(25)


def rand_walk(n):
    for _ in range(n):
        num = random.randint(0, 20)

        if num % 2 == 0:
            right_forward()
            timmy.color(random.choice(colors))
        if num % 3 == 0:
            left_forward()
            timmy.color(random.choice(colors))


rand_walk(20)


screen.exitonclick()

