from turtle import Turtle, Screen
import random as rd


def random_color():
    return(rd.random(), rd.random(), rd.random())


def walk(step : int, t : Turtle):
    possibilities = [0, 90, 180, 270]   
    for _ in range(step):
        t.color(random_color())
        t.right(rd.choice(possibilities))
        t.forward(10)


turtle = Turtle()
walk(200, turtle)

screen = Screen()
screen.exitonclick()