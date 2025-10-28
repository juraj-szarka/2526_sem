with open("pustatina_log.txt", encoding='utf-8') as f:
    f_list = f.readlines()

for i in range(len(f_list)):
    f_list[i].strip()

enters_num = len(f_list)
print(f'Počet záznamov: {enters_num}')

fixed_list = []
for i in f_list:
    fixed_list.append(i.split(' '))
avg_sum = 0
for i in fixed_list:
    avg_sum += float(i[2][4:])
avg = avg_sum/enters_num
print(f'Priemerná radiácia: {round(avg, 2)}')

locations = []
for i in fixed_list:
    loc = i[1][4:]
    if loc not in locations:
        locations.append(loc)
print('Lokality:')
for i in locations:
    print(i)

ghouls_num = 0
for i in fixed_list:
    if i[4][10:].strip() == 'ghoul':
        ghouls_num += 1
print(f'Počet ghoulov: {ghouls_num}')