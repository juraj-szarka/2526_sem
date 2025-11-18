import tkinter as tk

def sachovnica(n):
    for i in range(n):
        for j in range(n):
            stvorec(i*30, j*30, ('black' if (i+j)%2 else 'white'))

def stvorec(x, y, farba):
    canvas.create_rectangle(x, y, x+30, y+30, fill=farba)


canvas = tk.Canvas()

sachovnica(10)

canvas.pack()

tk.mainloop()