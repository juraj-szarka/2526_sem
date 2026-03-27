minn = int(input('enter min: '))
maxn = int(input('enter max: '))
total = 0

for i in range(minn, maxn):
    j = 2
    active = True
    while j <= i ** 0.5 and active:
        if i % j == 0:
            active = False
        j += 1
    if active:
        print(i)
        total += 1
        
print('there is', total, 'primes in range betwen', minn, 'and', maxn)
    