import random
import tkinter as tk

a = []
for i in range(5):
    a.append(random.randrange(30, 60))
    
canvas = tk.Canvas()

canvas.create_line(20, 20, 20, 80)
canvas.create_line(20, 80, 80, 80)

for i in range(len(a)):
    canvas.create_rectangle(30+i*20, 80-a[i], 45+i*20, 80)
    canvas.create_rectangle(30+i*20, 90, 46+i*20, 106, fill=random.choice)
    canvas.create_text(f'{a[i]}', 38+i*20, 98)



canvas.pack()
tk.mainloop()