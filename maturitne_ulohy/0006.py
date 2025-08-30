import tkinter as tk

f = open("content/noty.txt", "r")
notes = f.read()

def musical_score(x=20, w=800, padding=20, lines=1):
    for j in range(x, x+1+lines*80, 80):
        for i in range(0, 41, 10):
            canvas.create_line(padding, i+j, w-padding, i+j)

def create_note(note, offset=0, note_index=0, color="black"):
    y = 0
    x = 30 + note_index * 40
    ind = 65 + offset * 80
    if note == "c":
        y = 0 + ind
    elif note == "d":
        y = -5 + ind
    elif note == "e":
        y = -10 + ind
    elif note == "f":
        y = -15 + ind
    elif note == "g":
        y = -20 + ind
    elif note == "a":
        y = -25 + ind
    elif note == "h":
        y = -30 + ind

    print(x, y)

    canvas.create_arc(
        22+x, 0+y, 42+x, 20+y,
        start=30,
        extent=120,
        style=tk.ARC,
        outline=color
    )

    canvas.create_arc(
        22+x, y-10, 42+x, 10+y,
        start=-30,
        extent=-120,
        style=tk.ARC,
        outline=color
    )

def write(tones):
    lines = len(tones)//18
    if len(tones) % 18 != 0:
        lines += 1
    musical_score(lines=lines)
    myindex = 0
    myline = 0
    for i in range(len(tones)):
        if myindex % 18 == 0 and myindex != 0:
            myindex = 0
            myline += 1
        print(myline, myindex)
        create_note(tones[i-myline*18], note_index=myindex, offset=myline)
        myindex += 1
    return None


canvas = tk.Canvas(width=800, height=800)
canvas.pack()

write(notes)


canvas.mainloop()
