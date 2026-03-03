twnty = 0
dbl = 0

for i in range(int(input('zadaj pocet dni: '))):
    twnty += 20
    dbl += 2 ** i
    
    
if twnty > dbl:
    print('viac sa ti oplati dvadsad eur')
else:
    print('viac sa oplati dvojnasobok')
    
print('twnty', twnty, 'dbl', dbl)