from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
# screen.screensize(300, 300)
screen.setup(402, 400)

colors = [
    (122, 161, 207), (231, 159, 74), (38, 107, 170), (190, 135, 173), (14, 24, 81), (202, 78, 125),
    (149, 96, 53), (38, 40, 133), (235, 202, 100), (97, 106, 190), (154, 61, 106), (168, 167, 231),
    (168, 14, 41), (228, 160, 201), (121, 166, 131), (229, 88, 44), (52, 6, 28), (158, 218, 153),
    (197, 134, 36), (73, 167, 102), (42, 158, 200), (162, 203, 216), (11, 95, 103), (249, 217, 1),
    (11, 41, 39), (70, 118, 100)
]

colors_a = [
    (149, 9, 82), (94, 0, 53), (2, 2, 2), (2, 54, 24), (0, 92, 105), (196, 144, 209),
    (172, 172, 222), (171, 218, 252)
]


def paint(number_of_dots):
    tim.penup()
    tim.goto(-190, -180)
    x = -190
    y = -180
    tim.goto(x, y)
    for a in range(0, number_of_dots):
        for b in range(0, number_of_dots):
            tim.dot(20, random.choice(colors_a))
            tim.fd(40)
        y += 40
        tim.goto(x, y)


paint(10)
screen.exitonclick()
print(screen.screensize())