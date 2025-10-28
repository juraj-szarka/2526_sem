''' Zadanie 7 – Cyklopočítač
Počas hodinového cyklistického tréningu cyklopočítač cyklistu v pravidelných minútových intervaloch meria nadmorskú výšku (v metroch) a vzdialenosť od posledného merania (v metroch).
---
- Vytvorte program, ktorý si údaje o takomto tréningu vygeneruje a niekam uloží (pole alebo textový súbor).
- Vypočíta a vypíše pre trénera celkovú dĺžku dráhy.
- Vypočíta a vypíše priemernú rýchlosť cyklistu.
- Zistí a vypíše najväčšiu nadmorskú výšku.
- Zistí a vypíše koľko minút po začiatku sa cyklista ocitol na mieste s najvyššou nadmorskou výškou.
'''


import random
log = []

for i in range(60):
    log.append([random.randint(100, 1500), random.randint(200, 600)])

length = 0
max_elv = 0
max_elv_place = 0
for i in log:
    length += i[0]
    if i[1] > max_elv:
        max_elv = i[1]
        max_elv_place = log.index(i)

print('distance travelled: ', length, 'm')
print('average speed: ', round((length/len(log)/60*3.6), 1), 'km*h^-1')
print('max elevation: ', max_elv, 'm  in minute: ', max_elv_place)
