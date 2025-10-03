import tkinter

canvas = tkinter.Canvas()
canvas.pack()

f = open('content/stickman.txt', 'r')
coords = f.read().split('\n')

canvas.create_oval(int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]))

for i in range(4, len(coords), 4):
    canvas.create_line(int(coords[i]), int(coords[i+1]), int(coords[i+2]), int(coords[i+3]))

tkinter.mainloop()
