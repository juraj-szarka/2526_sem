import tkinter as tk

from reportlab.graphics.samples.excelcolors import backgroundGrey


def positive():
    f = open('content/reviews.txt', 'a')
    f.write('Áno\n')
    f.close()

def negative():
    f = open('content/reviews.txt', 'a')
    f.write('Nie\n')
    f.close()

root = tk.Tk()
root.title('Customer feedback')
root.geometry('300x200')


label = tk.Label(root, text='Boli ste spokojný s našími službami?', font=('Arial', 12, 'bold'))
label.pack(pady=30)

frame = tk.Frame(root)
frame.pack(expand=True)

button = tk.Button(frame, text = "Áno", command=positive, background='green')
button.pack(padx=10, side=tk.LEFT)

button = tk.Button(frame, text = "Nie", command=negative, background='red')
button.pack(padx=10, side=tk.LEFT)

root.mainloop()
