N = input('Zadaj pocet znakov (3 - 30): ')
Z = input('Zadaj znak: ')

for i in range(int(N)):
    print((int(N) - i) * Z)