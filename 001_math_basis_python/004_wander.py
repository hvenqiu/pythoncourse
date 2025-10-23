from turtle import *
from random import randint

shape("turtle")
speed(0)
def wander():
    while True:
        fd(3)
        if xcor() > 200 or xcor() < -200 or ycor() > 200 or ycor() < -200:
            # 转向更大的角度，并后退一步回到边界内
            bk(3)
            lt(randint(90,180))

wander()

done()