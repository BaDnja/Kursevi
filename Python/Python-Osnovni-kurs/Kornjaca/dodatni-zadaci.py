
# ZADACI
# Slovo N latinicom
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-kornjacazadaci#n
'''
from turtle import *
left(90)
forward(100)
right(135)
forward(141)
left(135)
forward(100)
'''

# Kvadratna spirala
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-kornjacazadaci#id4
'''
import turtle, random
n = 50
a = 5
boje = ["purple", "red", "green", "blue", "yellow", "orange", "black"]
turtle.speed(5)

for i in range(n):
    for i in range(4):
        turtle.color(random.choice(boje))
        turtle.left(90)
        turtle.forward(a)
        a = a + 5
        turtle.color(random.choice(boje))
        turtle.left(90)
        turtle.forward(a)
        a = a + 5
'''

# N-tougaona spirala
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-kornjacazadaci#id6
'''
import turtle, random
n = 10
a = 2
u = 8
boje = ["purple", "red", "green", "blue", "yellow", "orange", "black"]
turtle.speed(0)

for i in range(n):
    for i in range(u):
        turtle.color(random.choice(boje))
        turtle.left(360/u)
        turtle.forward(a)
        turtle.color(random.choice(boje))
        turtle.left(360/u)
        turtle.forward(a)
        a = a + 2
'''

# Osmokrake zvijezde u tjemenima osmougla
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-kornjacazadaci#id8
'''
import turtle, random

boje = ["purple", "red", "green", "blue", "orange", "black"]
turtle.speed(0)
n = 8
a = 60

def zvezda8(a):
    turtle.color(random.choice(boje))
    for i in range(8):
        turtle.forward(a/2)
        turtle.right(135)

for i in range(n):
    turtle.color(random.choice(boje))
    turtle.forward(a)
    turtle.left(360/n)
    zvezda8(a)
'''
