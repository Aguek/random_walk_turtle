import turtle
from turtle import Turtle, Screen
from random import choice

screen = Screen()
timmy = Turtle()
turtle_colors = ["blue", "yellow", "black", "orange", "red", "green"]
angles = [0, 90, 180, 270]

for _ in range(720):
    turtle.speed("fastest")
    direction = choice(angles)
    timmy.pensize(10)
    timmy.forward(30)
    timmy.setheading(direction)
    timmy.color(choice(turtle_colors))


screen.exitonclick()
