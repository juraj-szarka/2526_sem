import random

print('veky: ')
ages = []
for i in range(10):
    ages.append(random.randint(15, 25))
    print(ages[-1])
    
print('ziakov je ', len(ages))

twnty = 0
adult
for i in ages():
    if i == 20:
        twnty += 1
    if i >= 18:
        adult += 1
    
print('dvatsiatnikov je:', twnty)
print('dospelych je:', adult)
