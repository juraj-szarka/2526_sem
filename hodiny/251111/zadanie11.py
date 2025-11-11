import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

with open("kresli.txt", "r") as f:
    lines = f.readlines()
for line in lines:
    parts = line.split(' ')
    for i in range(0, len(parts)-2, 2):
        canvas.create_line(int(parts[i]), int(parts[i+1]), int(parts[i+2]), int(parts[i+3]))

root.mainloop()