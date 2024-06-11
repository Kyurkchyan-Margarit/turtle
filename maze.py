import turtle
import random

# Constants
CELL_SIZE = 20
MAZE_SIZE = 9

# Maze grid
maze = [[0] * MAZE_SIZE for _ in range(MAZE_SIZE)]

# Turtle settings
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("white")

# Function to draw a rectangle at the given position
def draw_rectangle(x, y, color="white"):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(CELL_SIZE)
        turtle.right(90)
    turtle.end_fill()

# Function to draw the maze
def draw_maze():
    for i in range(MAZE_SIZE):
        for j in range(MAZE_SIZE):
            if maze[i][j] == 1:  # Wall
                draw_rectangle(j * CELL_SIZE, -i * CELL_SIZE, "black")
            else:  # Path
                draw_rectangle(j * CELL_SIZE, -i * CELL_SIZE)

# Recursive Backtracking algorithm for maze generation
def generate_maze(x, y):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx * 2, y + dy * 2

        if 0 <= nx < MAZE_SIZE and 0 <= ny < MAZE_SIZE and maze[ny][nx] == 0:
            maze[y + dy][x + dx] = 1
            maze[ny][nx] = 1
            generate_maze(nx, ny)

# Depth-First Search algorithm for maze solving
def solve_maze(x, y):
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE and maze[y][x] == 0:
        maze[y][x] = 2  # Mark the cell as visited

        # Draw the solution path
        draw_rectangle(x * CELL_SIZE, -y * CELL_SIZE, "yellow")

        # Explore in all directions
        solve_maze(x + 1, y)
        solve_maze(x - 1, y)
        solve_maze(x, y + 1)
        solve_maze(x, y - 1)

# Main function
def main():
    turtle.title("Maze Generation and Solving")
    turtle.setup(width=MAZE_SIZE * CELL_SIZE, height=MAZE_SIZE * CELL_SIZE)

    generate_maze(0, 0)
    draw_maze()

    turtle.penup()
    turtle.goto(CELL_SIZE // 2, -CELL_SIZE // 2)
    turtle.pendown()
    turtle.color("red")

    solve_maze(0, 0)

    turtle.done()

if __name__ == "__main__":
    main()