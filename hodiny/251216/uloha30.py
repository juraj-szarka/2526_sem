import tkinter as tk

canvas = tk.Canvas()

for i in range(10):
    for j in range(10):
        if i-j > 0:
            canvas.create_rectangle(10+i*20, 10+j*20, 30+i*20, 30+j*20, outline="green")
        else:
            canvas.create_oval(10+i*20, 10+j*20, 30+i*20, 30+j*20, outline="yellow")
        


canvas.pack()

tk.mainloop()
