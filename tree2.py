import tkinter as tk
import math

class Tree(tk.Canvas):
    def __init__(self, depth):
        super().__init__(width=900, height=800, background='black')
        self.depth = depth
        self.pack()
        self.draw_fractal_tree(self.winfo_reqwidth() / 2, self.winfo_reqheight(), depth, -90)

    def draw_fractal_tree(self, x1, y1, depth, angle):
        if depth == 0:
            return

        length = 100
        x2 = x1 + int(math.cos(math.radians(angle)) * 13 * depth)
        y2 = y1 + int(math.sin(math.radians(angle)) * 13 * depth)
        din_color = f'#{255 - 20 * depth:02x}00{20 * depth:02x}'


        self.create_line(x1, y1, x2, y2, fill=din_color)

        self.draw_fractal_tree(x2, y2, depth - 1, angle + 20)
        self.draw_fractal_tree(x2, y2, depth - 1, angle - 30)
        self.draw_fractal_tree(x2, y2, depth - 1, angle - 10)

        if depth == 1 or depth == 2:
            self.create_oval(x2 - 6, y2 - 3, x2 + 6, y2 + 3, fill='orange')

def main():
    root = tk.Tk()
    root.title("Fractal Tree")
    fractal_tree = Tree(9)  # Adjust depth as needed
    fractal_tree.mainloop()

if __name__ == "__main__":
    main()
