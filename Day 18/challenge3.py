from turtle import Turtle, Screen
import random as rd

def random_color():
    return(rd.random(), rd.random(), rd.random())

def draw_decagon(t : Turtle):
    t.color(random_color())
    for _ in range(10) :
        t.right(360/10)
        t.forward(100)

def draw_nonagon(t : Turtle):
    t.color(random_color())
    for _ in range(9) :
        t.right(360/9)
        t.forward(100)

def draw_octagon(t : Turtle):
    t.color(random_color())
    for _ in range(8) :
        t.right(360/8)
        t.forward(100)

def draw_heptagon(t : Turtle):
    t.color(random_color())
    for _ in range(7) :
        t.right(360/7)
        t.forward(100)

def draw_hexagon(t : Turtle):
    t.color(random_color())
    for _ in range(6) :
        t.right(360/6)
        t.forward(100)

def draw_pentagon(t : Turtle):
    t.color(random_color())
    for _ in range(5) :
        t.right(360/5)
        t.forward(100)

def draw_square(t : Turtle):
    t.color(random_color())
    for _ in range(4) :
        t.right(360/4)
        t.forward(100)

def draw_triangle(t : Turtle):
    t.color(random_color())
    for _ in range(3) :
        t.right(360/3)
        t.forward(100)

turtle = Turtle()
draw_triangle(turtle)
draw_square(turtle)
draw_pentagon(turtle)
draw_hexagon(turtle)
draw_heptagon(turtle)
draw_octagon(turtle)
draw_nonagon(turtle)
draw_decagon(turtle)

screen = Screen()
screen.exitonclick()