import random

with open('otazky.txt', 'r') as file1:
    questions = file1.readlines()

test = ''
for i in range(min(5, len(questions))):
    test += questions.pop(random.randint(0, len(questions)-1))

with open('test.txt', 'w') as file2:
    file2.write(test)
print(test)                  
