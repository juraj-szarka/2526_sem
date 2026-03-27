import random
import tkinter

lh = random.randint(10, 3600)
ld = 0
max_h = lh
max_t = 0
data = [[lh, ld]]
ec = random.uniform(0, 24)

for i in range(60):
    hc = random.randint(-25, 150)
    if hc > 0:
        hc //= ec
    else:
        hc *= ec
    nh = min(max(10, lh+hc), 3600)
    nd = random.randint(80, 160) if nh > lh else random.randint(360, 2000)
    data.append([nh, nd])
    ld += nd
    lh = nh
    if nh > max_h:
        max_h = nh
        max_t = i
        
    
print(data)
    
print('max_h', max_h)
print('total l', ld/1000)
print('avg speed kmh', ld/1000)
print('max t', )

canvas = tkinter.Canvas(width=2000, height=1000)
canvas.pack()

cur_l = data[0][1]
cur_h = data[0][0]

print(cur_l)
print(cur_h)

for i in range(1, len(data)):
    print(cur_l/15, cur_h/10, (cur_l + data[i][1])/15, data[i][0]/10)
    canvas.create_line(cur_l/15, 600-(cur_h/10), (cur_l + data[i][1])/15, 600-(data[i][0]/10))
    cur_l += data[i][1]
    cur_h = data[i][0]
    
print(ec)

tkinter.mainloop()

