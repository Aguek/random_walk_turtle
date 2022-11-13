import turtle
from turtle import Turtle, Screen
from random import choice

screen = Screen()
timmy = Turtle()
angles = [0, 90, 180, 270]
#setting the colormode to accept RGB
turtle.colormode(255)

#method to generate automatic RGB values for the RGB colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for _ in range(720):
    turtle.speed("fastest")
    direction = choice(angles)
    timmy.pensize(10)
    timmy.forward(30)
    timmy.setheading(direction)
    timmy.color(random_color()


screen.exitonclick()
