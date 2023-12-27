import turtle
import random


def draw_triangle(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
        if _ != 1:
            color = random.choice(["red",
                                   "yellow",
                                   "blue",
                                   "orange"])
            turtle.dot(10, color)
    turtle.end_fill()


def draw_tree(levels):
    base_size = 30
    trunk_height = 50
    triangle_color = "green"
    trunk_color = "brown"

    turtle.speed(5)
    turtle.bgcolor("#071330")
    turtle.penup()
    turtle.goto(-base_size * levels / 2, -150)
    turtle.pendown()

    # Draw tree
    for level in range(1, levels):
        draw_triangle(base_size *
                      (levels - level),
                      triangle_color)
        turtle.penup()
        turtle.goto(0 - base_size *
                    (levels - level) / 2,
                    -150 + (level * base_size)
                    + (level * base_size) * 0.10)
        turtle.pendown()

    turtle.penup()
    turtle.color("yellow")
    turtle.goto(0 - base_size - 5,
                -145 + (levels * base_size))
    turtle.begin_fill()
    turtle.pendown()

    for i in range(5):
        turtle.forward(40)
        turtle.right(144)

    turtle.end_fill()

    # Draw trunk
    turtle.penup()
    turtle.goto(-35, -150)
    turtle.pendown()
    turtle.color(trunk_color)
    turtle.fillcolor(trunk_color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(trunk_height)
        turtle.right(90)
    turtle.end_fill()

    turtle.hideturtle()
    turtle.done()


def draw_light(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(10, color)


# Adjust the number of levels as per your preference
draw_tree(levels=10)
