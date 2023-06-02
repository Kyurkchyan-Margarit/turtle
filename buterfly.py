import turtle


def wings(r):
    turtle.up()
    turtle.setpos(r - 100, 100 - r)
    turtle.down()
    turtle.begin_fill()

    for i in range(4):
        turtle.left(90)
        turtle.circle(r, 180)
    turtle.end_fill()


def legs(pos):
    turtle.up()
    turtle.left(90 if pos == 1 else -135)
    turtle.setpos(-100, 100)
    turtle.down()
    turtle.color('#000000', '#000000')
    turtle.circle(170, 50 * pos)
    turtle.right(90 * pos)
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()


turtle.color('#FF0000', '#000000')
wings(120)
# turtle.color('#FF0000', '#FFFFFF')
# wings(100)
# turtle.color('#FF0000', '#FFB6C1')
# wings(90)
# turtle.color('#FF0000', '#808080')
# wings(80)
turtle.color('#FF0000', '#FFB6C1')
wings(70)
turtle.color('#FF0000', '#C0C0C0')
wings(40)
# turtle.color('#FF0000', '#FFB6C1')
# wings(30)
turtle.color('#FF0000', '#808080')
wings(20)
# legs(1)
# legs(-1)
turtle.ht()
turtle.done()
