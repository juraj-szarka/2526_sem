import random

months = [random.randint(0, 100) for i in range(12)]\
         
for i in range(len(months)):
    print(i+1, ':', months[i])

print('average:', round((sum(months) / 12), 2))