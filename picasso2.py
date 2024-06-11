import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle instance
kaleidoscope = turtle.Turtle()
kaleidoscope.speed(0)  # Fastest speed

# Set colors
colors = ["red", "green", "blue", "orange", "purple", "yellow"]
# colors = ["green", "blue", "green", "blue", "green", "blue"]

# Draw kaleidoscope pattern
for angle in range(0, 360, 15):
    kaleidoscope.color(colors[angle // 60])
    kaleidoscope.penup()
    kaleidoscope.goto(0, 0)
    kaleidoscope.pendown()
    kaleidoscope.setheading(angle)
    kaleidoscope.forward(100)
    kaleidoscope.setheading(180 - angle)
    kaleidoscope.forward(200)
    kaleidoscope.setheading(180 + angle)
    kaleidoscope.forward(100)
    kaleidoscope.setheading(360 - angle)
    kaleidoscope.forward(200)

# Hide the turtle
kaleidoscope.hideturtle()

# Exit on click
turtle.done()
