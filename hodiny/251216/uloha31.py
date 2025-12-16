h = 0
d = input('zadaj dolnu hranicu: ')
while int(h) < int(d):
    h = input('zadaj hornu hranicu: ')

for i in range(int(d), int(h)+1):
    if i % 6 == 0:
        print(i)