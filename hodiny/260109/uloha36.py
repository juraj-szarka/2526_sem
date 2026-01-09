sentence = input('Zadaj vetu: ')
x = input('Zadaj znak: ')

for i in range(len(sentence)):
    if sentence[i] == ' ':
        sentence = sentence[0:i] + x + sentence[i+1:]
        
print(sentence)        
