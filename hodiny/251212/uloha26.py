name = input('Zadaj meno ziaka: ')
marks_string = input('Zadaj znamky: ')

marks = []
for i in marks_string:
    if i == '1' or i == '2' or i == '3' or i == '4' or i == '5':
        marks.append(int(i))
        
summ = 0
for i in marks:
    summ += i
    
print(f'{name}: {summ / len(marks)}')