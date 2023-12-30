import turtle
import random


def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


turtle.speed(15)
turtle.bgcolor("#071330")

draw_circle('white', 80, 0, -80)
draw_circle('white', 60, 0, 30)
draw_circle('white', 40, 0, 110)

draw_circle("#450711", 6, -17, 115)
draw_circle("#450711", 6, 17, 115)

turtle.penup()
turtle.goto(3, 110)
turtle.begin_fill()
turtle.pendown()
turtle.color("#ee7600")
turtle.right(65)
turtle.forward(10)
turtle.right(150)
turtle.forward(10)
turtle.right(90)
turtle.forward(5)
turtle.end_fill()

turtle.pencolor("black")
draw_circle("#450711", 2, -6, 93)
draw_circle("#450711", 2, 0, 90)
draw_circle("#450711", 2, 6, 90)
draw_circle("#450711", 2, 12, 93)

turtle.penup()
turtle.goto(40, 125)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.begin_fill()
turtle.left(50)
for _ in range(3):
    turtle.forward(75)
    turtle.left(120)
turtle.end_fill()
turtle.goto(40, 135)
turtle.color("green")
turtle.width(4)
turtle.left(60)
for _ in range(8):
    turtle.circle(6)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

turtle.penup()
turtle.goto(26, 210)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.color('#8e4b21')
turtle.penup()
turtle.goto(60, 50)
turtle.pendown()
turtle.width(5)
turtle.left(40)
turtle.backward(60)

turtle.penup()
turtle.goto(-60, 50)
turtle.pendown()
turtle.right(40)
turtle.forward(60)

turtle.width(3)
turtle.penup()
turtle.goto(-80, 55)
turtle.pendown()
turtle.right(40)
turtle.forward(20)

turtle.penup()
turtle.goto(-100, 60)
turtle.pendown()
turtle.left(70)
turtle.forward(20)

turtle.penup()
turtle.goto(80, 55)
turtle.pendown()
turtle.right(40)
turtle.backward(20)

turtle.color('white')
for i in range(100):
    turtle.penup()
    turtle.goto(random.randint(-500, 500),
                random.randint(-500, 500))
    turtle.pendown()
    turtle.circle(2)

turtle.hideturtle()
turtle.mainloop()
