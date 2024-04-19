from random import randint, choice
from turtle import *

speed(0)
for i in range(100):
    colormode(255)
    fillcolor(randint(0, 255),randint(0, 255),randint(0, 255))
    begin_fill()
    circle(randint(50, 150))
    end_fill()
    goto(randint(-255, 255), randint(-255, 255))

done()