from turtle import *

shape("turtle")
# right(45)
# forward(150)
# speed(1)

def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)

# for i in range(60):
#     square(150)
#     right(6)

# length = 100
# for i in range(60):
#     square(length)
#     right(6)
#     length += 5

# square(50)
# square(80)
# square()

# def triangle(sidelength=100):
#     for i in range(3):
#         forward(sidelength)
#         right(120)

# triangle(100)

# def polygon(sidelength=100, sides=3):
#     for i in range(sides):
#         forward(sidelength)
#         right(360/sides)

# polygon(100, 20)

def star(sidelength=100 , points=5):
    for i in range(points):
        forward(sidelength)
        right(180 - 180/points)

star(points=3)

done()