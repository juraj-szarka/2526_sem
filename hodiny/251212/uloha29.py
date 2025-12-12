n1 = int(input('Zadaj cislo 1: '))
n2 = int(input('Zadaj cislo 2: '))
op = None

while op != '+' and op != '-' and op != '*' and op != '/':
    op = input('Zadaj operaciu: ')
    
if op == '+':
    print(n1 + n2)
if op == '-':
    print(n1 - n2)
if op == '*':
    print(n1 * n2)
if op == '/':
    print(n1 / n2)