import tkinter as tk
import random

root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack()

p = 0

for i in range(5):
    for j in range(10):
        o = random.randint(0, 8)
        p += o
        w = 10
        d = 30
        x = 50 + j * d
        y = 50 + i * d
        canvas.create_rectangle(x-w, y-w, x+w, y+w, fill=("yellow" if o == 0 else None))
        canvas.create_text(x, y, text=o)
canvas.create_text(20, 200, text=p)

root.mainloop()