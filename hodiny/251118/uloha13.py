import random
import math

num = random.randint(0, 255)
print('num: ', num)
num_bin = ''

for i in range(8):
    if num >= 2 ** (7 - i):
        num -= 2 ** (7-i)
        num_bin += ('1')
    else:
        num_bin += ('0')
        
print(num_bin)