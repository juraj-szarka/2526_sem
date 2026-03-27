with open('slovencina.txt', 'r', encoding='UTF-8') as file:
    text = file.readlines()
    
print(text)
letters_pre = text[0].strip()
text = text[1:]
text3 = ''
for j in text:
    text2 = j
    print(text2)
    for i in text2:
        if i in letters_pre:
            text3 += '_'
        else:
            text3 += i
print(text3)

with open('slovencina_vystup_b.txt', 'w', encoding='UTF-8') as file:
    file.write(text3)