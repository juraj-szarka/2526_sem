veta = input('zadajte vetu: ')
slab = input('zadajte hladanu slabiku: ')

count = 0
for i in range(len(veta) - len(slab) + 1):
    if veta[i:(i+len(slab))] == slab:
        count += 1
        
if count:
    print(f'zadana slabika sa v texte nachadza {count}')
else:
    print('zadana slabika sa v texte nenasla')

