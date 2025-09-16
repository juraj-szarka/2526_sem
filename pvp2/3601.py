f = open('content/tabulkaznakov.txt', 'w')
index = 97
while index <= 122:
    f.write(f'{chr(index)} {index}\n')
    index += 1
f.close()