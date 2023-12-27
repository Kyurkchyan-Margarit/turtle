import turtle
import math


class Tree(turtle.Turtle):
    def __init__(self, depth):
        super().__init__()
        self.depth = depth
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.speed(0)
        self.hideturtle()

    def fractal_tree(self, x1, y1, depth, angle):
        if depth == 0:
            return

        x2 = x1 + int(math.sin(math.radians(angle))
                      * 13 * depth)
        y2 = y1 + int(math.cos(math.radians(angle))
                      * 13 * depth)

        self.penup()
        self.goto(x1, y1)
        self.pendown()
        self.pensize(depth)
        self.pencolor('green')
        self.goto(x2, y2)

        self.fractal_tree(x2, y2, depth - 1, angle + 20)
        self.fractal_tree(x2, y2, depth - 1, angle - 40)
        self.fractal_tree(x2, y2, depth - 1, angle - 10)

        if depth == 1 or depth == 2:
            self.penup()
            self.goto(x2, y2)
            self.pendown()
            self.pencolor('orange')
            self.fillcolor('orange')
            self.begin_fill()
            self.circle(2)
            self.end_fill()


    def draw_tree(self):
        self.fractal_tree(0, -200, self.depth, 0)
        self.screen.exitonclick()


def main():
    fractal_tree = Tree(7)
    fractal_tree.draw_tree()

if __name__ == "__main__":
    main()