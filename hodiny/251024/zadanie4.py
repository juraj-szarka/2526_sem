with open("zamestnanci.txt", encoding='utf-8') as f:
    f_list = f.readlines()

for i in range(len(f_list)):
    f_list[i] = f_list[i].strip()

command = input('Zadaj prikaz (PARNE / PIATI / POCET): ')

if command.strip().lower() == 'parne':
    for i in range(1, len(f_list), 2):
        print(f_list[i])
elif command.strip().lower() == 'piati':
    sp = input('Zadaj pociatocne meno: ')
    if sp in f_list:
        idx = f_list.index(sp)
        for i in range(idx, (idx+5)%len(f_list), 1):
            print(f_list[i])
elif command.strip().lower() == 'pocet':
    free = int(input('Zadaj pocet volnych miest: '))
    for i in range(-1, -free-1, -1):
        print(f_list[i])

# print(f_list)