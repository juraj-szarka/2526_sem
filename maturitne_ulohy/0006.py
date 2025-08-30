import tkinter as tk

def musicalscore(x=20, w=400, padding=20):
    for i in range(0, 21, 5):
        canvas.create_line(padding, x+i, w-padding, x+i)

canvas = tk.Canvas(width=400, height=400)
canvas.pack()

musicalscore()

canvas.mainloop()