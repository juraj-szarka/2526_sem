import tkinter as tk
import random

coords = []

def on_click(event):
    canvas.create_oval(event.x-2, event.y-2, event.x+2, event.y+2)
    global coords
    if not coords:
        coords = [event.x, event.y]
    else:
        canvas.create_line(event.x, event.y, coords[0], coords[1])
        coords = [event.x, event.y]

def add_point(x, y):
    canvas.create_oval(x-2, y-2, x+2, y+2)
    global coords
    if not coords:
        coords = [x, y]
    else:
        canvas.create_line(x, y, coords[0], coords[1])
        coords = [x, y]


root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack()

for i in range(500):
    add_point(random.randint(0, 500), random.randint(0, 500), i)


canvas.bind("<Button-1>", on_click)

root.mainloop()