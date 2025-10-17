import random
import tkinter as tk

w = random.randint(200, 600)
h = w

canvas = tk.Canvas(width=w, height=h)
canvas.pack()

def paint(width):
    a = 10
    x = 10
    while (x + a) < width:
        canvas.create_rectangle(x, width/2-a, x+a, width/2)
        x += a
        a += 5

paint(w)

tk.mainloop()