import tkinter as tk

f = open('content/zastavky.txt', 'r', encoding='utf-8')

zastavky = f.read()

def load_stations(stations = zastavky):
    stations_1 = stations.split('\n')
    for i in range(len(stations_1) - 1):
        if len(stations_1[i]) < 16:
            stations_1[i] += (20 - len(stations_1[i])) * ' '
        else:
            stations_1[i] += 4 * ' '
    stations_1[-1] += '    konečná zástavka, prosíme nenastupovať    '
    print(stations_1)

stations_displayable = []

canvas = tk.Canvas()
canvas.pack()

load_stations()

canvas.mainloop()