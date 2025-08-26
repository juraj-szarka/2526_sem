import tkinter as tk
import time

f = open('content/zastavky.txt', 'r', encoding='utf-8')

zastavky = f.read()
station_index = 0
stations = []
current = ''
state = 0
instances = []

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
            to_append += staged_text[j+i]
        loaded.append(to_append)

    return loaded

def rewrite_text():
    global text
    canvas.delete(text)
    text = canvas.create_text(200, 25, font=('Courier', 24), text=current, fill='red')



def roll():
    global current
    global state
    global instances
    current = instances[state]
    print(instances)
    print(instances[state])
    rewrite_text()
    if (state + 1) == len(instances):
        state = 0
    else:
        state += 1
    canvas.after(250, roll)

def start():
    global stations
    global station_index
    global current
    global state
    global instances
    global text
    station_index = 0
    stations = load_stations(zastavky)
    current = stations[0]
    state = 0
    instances = load_instance(stations[station_index])
    text = canvas.create_text(200, 25, font=('Courier', 24), text=current, fill='red')
    roll()
    print('done')
    return None

def on_click(event):
    global station_index
    global current
    global stations
    global state
    global instances
    state = 0

    if station_index == (len(stations) - 1):
        station_index = 0
    else:
        station_index += 1

    instances = load_instance(stations[station_index])
    return None

canvas = tk.Canvas(width=400, height=50, background='black')
canvas.pack()
start()

canvas.bind('<Button-1>', on_click)


canvas.mainloop()