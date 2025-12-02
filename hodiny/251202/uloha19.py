import random

box = []
for i in range(10):
    box.append(random.randint(0, 15))
    
if 4 not in box:
    print('červená sa tu nenachádza vo valci')
else:
    for i in range(-1, -10, -1):
        if box[i] == 4:
            print(abs(i))
            break
