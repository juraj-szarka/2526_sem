from turtle import *

# Funkcie na kreslenie sviečok - doplňte ich telá
def obdlznik(sirka, vyska):
    for i in range(4):
        if i % 2:
            fd(vyska)
        else:
            fd(sirka)
        rt(90)        

def trojuholnik(strana):
    for _ in range(3):
        fd(strana)
        lt(120)

def sviecka(sirka, vyska):
    obdlznik(sirka, vyska)
    fd(sirka/4)
    trojuholnik(sirka/2)
    
    
    
def skoc_na(x,y):
    pu()
    setpos(x,y)
    setheading(0)
    pd()

# Hlavný program - nastavenie pera
pd()
pensize(3)

# dorobte tu zvyšok programu - treba tri náhodne umiestnené sviečky rôznych veľkostí

skoc_na(-200, 50)
sviecka(30, 80)

skoc_na(0, 50)
sviecka(10, 300)

skoc_na(200, 50)
sviecka(300, 20)

done()
