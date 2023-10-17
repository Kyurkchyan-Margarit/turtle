import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle instance
artist = turtle.Turtle()
artist.speed(10)  # Set the drawing speed (1 = slowest, 10 = fastest)
artist.pensize(2)  # Set the pen size

# Set up colors
colors = ["red", "blue", "green", "orange", "purple"]

# Draw the abstract pattern
for i in range(360):
    artist.pencolor(colors[i % len(colors)])  # Switch color for each iteration
    artist.forward(i)
    artist.right(98)

# Hide the turtle
artist.hideturtle()

# Exit the turtle program when the screen is clicked
screen.exitonclick()
