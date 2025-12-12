from turtle import *

def trojuh(strana):
    for i in range(3):
        fd(strana)
        lt(120)
    fd(strana)

def hviezda(pocet, strana):
    for _ in range(pocet):
        trojuh(strana)
        rt(360/pocet)

def skoc():
    pass

pencolor('gold')
pensize(3)
speed(0)

hviezda(5, 30)

done()
