import turtle


def magic_function(r, pos, c1, c2):
    position = abs(turtle.pos())
    turtle.color(c1, c2)
    turtle.begin_fill()
    while True:
        turtle.circle(r, 180)
        turtle.left(pos)
        if int(position) == int(abs(turtle.pos())):
            break
    turtle.end_fill()


turtle.bgcolor("sky blue")
turtle.up()
turtle.goto(200, 200)
turtle.down()
magic_function(30, 150, '#FF0000', '#FCE570')
turtle.up()
turtle.goto(-100, -100)
turtle.down()
magic_function(60, 100, '#00AAFF', '#FFFFFF')
turtle.up()
turtle.goto(-28, -54.6)
turtle.down()
turtle.color('yellow', 'yellow')
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.up()
turtle.goto(-28, -112)
turtle.down()
turtle.color('green', 'green')
turtle.right(90)
turtle.forward(150)
turtle.up()
turtle.goto(-28, -170)
turtle.down()
turtle.begin_fill()
turtle.left(40)
turtle.circle(30, 150)
turtle.left(150)
turtle.circle(20, 150)
turtle.left(150)
turtle.circle(20, 150)
turtle.left(130)
turtle.circle(30, 150)
turtle.left(190)
turtle.circle(30, 75)

turtle.ht()
turtle.done()