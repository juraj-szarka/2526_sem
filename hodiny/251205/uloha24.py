from turtle import *
import random


# Dorobte telo funkcie obdlznik(sirka, vyska), ktora nakresli obdlznik so zadanymi rozmermi
def obdlznik(sirka, vyska):
    for i in range(4):
        if not i % 2:
            fd(vyska if vyska > sirka else sirka)
        else:
            fd(sirka if vyska > sirka else vyska)
        rt(90)
    rt(90)
    fd(sirka if vyska > sirka else vyska)
    lt(90)
    
pensize(2)
pencolor('brown')

# Dorobte 4 na sebe lezace obdlzniky tak, aby ležali položené na sebe dlhšej strane 
for i in range(4):
    vyska = random.randint(30, 100)
    sirka = random.randint(30, 100)
    obdlznik(sirka, vyska)

done()
