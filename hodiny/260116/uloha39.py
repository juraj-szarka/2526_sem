num = input('zadaj cislo medzi 200 as 300: ')
pal = []
tri = []
for i in range(int(num)):
    if str(i) == str(i)[::-1] and len(str(i)) > 2:
        pal.append(i)
        if not i % 3:
            tri.append(i)
print('PALINDROMI/Y')
for i in pal:
    print(i)
print('palindromov je', len(pal))
print('DELITELNE 3MI')
for i in tri:
    print(i)
print('palindromov delitelnych 3 je', len(tri))

