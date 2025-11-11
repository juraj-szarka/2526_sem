import tkinter as tk
import random
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

for i in range(21):
    for j in range(21):
        x = i * 20
        y = j * 20
        color = f'#{'000000' if random.randint(0, 1) == 0 else 'FFFFFF'}'
        canvas.create_rectangle(x, y, x + 20, y + 20, fill=color, outline='')

root.mainloop()