import tkinter as tk

f = open('content/zastavky.txt', 'r', encoding='utf-8')

zastavky = f.read()

canvas = tk.Canvas()
canvas.pack()

print(zastavky)

canvas.mainloop()