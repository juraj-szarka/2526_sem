from turtle import *

def kresli_domcek(x, y, size):
    goto(x, y)
    seth(0)
    for i in range(4):
        pd()
        fd(size)
        rt(90)
    seth(60)
    fd(size)
    rt(120)
    fd(size)

kresli_domcek(0, 0,100)