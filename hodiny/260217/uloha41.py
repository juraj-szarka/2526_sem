import tkinter
import random

canvas = tkinter.Canvas(width=1000, height=1000)
canvas.pack()

for i in range(10):
    n = random.randint(-3, 3)
    canvas.create_oval(i*30+10, 10, i*30+30+10, 30+10, fill = 'red' if n < 0 else ('green' if n > 0 else 'black'))
    canvas.create_text(i*30+25, 25, text=n, fill='white')

tkinter.mainloop()