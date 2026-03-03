r1 = input('zadaj prvy retazec: ')
r2 = input('zadaj druhy retazec: ')

correct = True
if len(r1) != len(r2):
    correct = False
    
for i in r1:
    if i not in r2:
        correct = False
        print('r1 a r2 sa neskladaju z rovnakych znakov')
        
