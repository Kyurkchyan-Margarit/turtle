import turtle

def draw_square(turtle_object, side_length):
    for _ in range(4):
        turtle_object.forward(side_length)
        turtle_object.right(90)


screen = turtle.Screen()
screen.title("Drawing Nested Squares")
my_turtle = turtle.Turtle()

for i in range(10):
    draw_square(my_turtle, 20 + i * 20)
    my_turtle.penup()
    my_turtle.goto(-10 * i, -10 * i)
    my_turtle.pendown()


screen.exitonclick()