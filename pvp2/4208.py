import tkinter

canvas = tkinter.Canvas()
canvas.pack()

f = open('content/kreslenie.txt', 'r')
coords = f.read()

coords = coords.split('\n')

for i in range(0, len(coords)-1, 2):
    canvas.create_oval(int(coords[i].strip())-5, int(coords[i+1].strip())-5, int(coords[i].strip())+5, int(coords[i+1].strip())+5)
    print(coords[i])

tkinter.mainloop()
