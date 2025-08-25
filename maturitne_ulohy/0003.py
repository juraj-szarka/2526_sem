import tkinter as tk

f = open('content/zastavky.txt', 'r', encoding='utf-8')

zastavky = f.read()
station_index = 0
stations = []
current = ''

def load_stations(stations = zastavky):
    stations_1 = stations.split('\n')
    for i in range(len(stations_1) - 1):
        if len(stations_1[i]) < 16:
            stations_1[i] += (20 - len(stations_1[i])) * ' '
        else:
            stations_1[i] += 4 * ' '
    stations_1[-1] += '    konečná zástavka, prosíme nenastupovať    '
    return stations_1

def load_instance(text: str):
    l = len(text)
    staged_text = 2*text
    loaded = []
    for i in range(l):
        to_append = ''
        for j in range(20):
            to_append += staged_text[j]
        loaded.append(to_append)

    return loaded

def rewrite_text():
    global text
    canvas.delete(text)
    text = canvas.create_text(200, 25, font=('Courier', 24), text=current, fill='red')



def start():
    global stations
    global station_index
    global current
    station_index = 0
    stations = load_stations(zastavky)
    current = stations[0]
    print('done')
    return None

def on_click(event):
    global station_index
    global current

    if station_index == (len(stations) - 1):
        station_index = 0
    else:
        station_index += 1
    current = stations[station_index]
    rewrite_text()
    print('clicked')
    print(station_index)
    print(current)
    return None

canvas = tk.Canvas(width=400, height=50, background='black')
canvas.pack()
start()

canvas.bind('<Button-1>', on_click)

text = canvas.create_text(200, 25, font=('Courier', 24), text=current, fill='red')

canvas.mainloop()