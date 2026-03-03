retazec = input('zadaj retazec: ')

n = 0
p = 0
stringodd = ''
stringeven = ''
for i in retazec:
    if i in '02468':
        p += 1
        stringeven += i
    elif i in '13579':
        n += 1
        stringodd += i

print('there is', n, 'odd numbers:', stringodd, 'and', p, 'even:', stringeven)