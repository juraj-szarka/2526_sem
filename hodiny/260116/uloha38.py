import random

cups = ['jed' for _ in range(2)]
cups[random.randint(0, 1)] = 'med'

print(cups[int(input('Vyberáš si pohár "1" alebo "2": ')) - 1])
print(cups)