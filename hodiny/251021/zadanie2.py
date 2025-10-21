import tkinter as tk

coords = []
points = []

def clear_canvas(event):
    canvas.delete("all")

def create_rectangle(event):
    global coords

    if not coords:
        coords = [event.x, event.y]
        points.append(canvas.create_oval(event.x-2, event.y-2, event.x+2, event.y+2))
    else:
        canvas.create_rectangle(coords[0], coords[1], event.x, event.y)
        coords = []
        canvas.delete(points[-1])
        points.pop(-1)
        print(points)

root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack()

canvas.bind("<Button-1>", create_rectangle)
canvas.bind("<Button-3>", clear_canvas)

root.mainloop()