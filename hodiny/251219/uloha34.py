import random

a = {}
for i in range(20):
    a[f'suciastka{i}'] = random.randint(0, 20)
    
    
b = {}
for i in a:
    print(i, ":", a[i])
    if a[i] != 0:
        b[i] = a[i]
        
print(f'je {len(a) - len(b)} vyradenych suciastok')

for i in b:
    print(i, ":", b[i])