import random

f = open('content/hesla.txt', 'w')

for i in range(int(input('zadaj pocet hesiel: '))):
    password = ''
    for _ in range(8):
        password += chr((random.randint(0, 25)) + 97)
    f.write(password + '\n')

f.close()