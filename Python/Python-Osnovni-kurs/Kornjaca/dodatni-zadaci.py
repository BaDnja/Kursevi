
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

# Zvijezde u tjemenima uglova n-tougla, na tjemenu jednakostraničnog trougla
'''
import turtle

def zvezda8(a):
    for i in range(8):
        turtle.forward(a/2)
        turtle.right(135)


def zvezdani_mnogougao(n, a):
    for i in range(n):
    	turtle.forward(a)
    	turtle.left(360/n)
    	zvezda8(a)

turtle.speed(0)
for i in range(3):
    zvezdani_mnogougao(i+4, 50)
    turtle.forward(180)
    turtle.left(120)
'''

# Linija od duži u tri boje, tri dužine
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-kornjacazadaci#id11
'''
import turtle
turtle.width(5)

linije = (('red', 15), ('green', 10), ('blue', 20))

for i in range(8):
    for elem in linije:
        turtle.color(str(elem[0]))
        turtle.forward(elem[1])
        turtle.left(15)
    turtle.color("orange")
    turtle.forward(30)
    turtle.right(90)
'''

# N-tokraka zvijezda bez presijecanja
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-kornjacazadaci#id13
'''
from turtle import *
#speed(0)

n = 8
nalijevo = 180-((n-2)*180/n)
nadesno = 2 * nalijevo

for i in range(n*2):
    forward(40)
    if i % 2 == 0:
        left(nalijevo)
    else:
        right(nadesno)
'''

# Tri kvadrata
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-kornjacazadaci#id15
'''
import turtle

boje = ("red", "green", "blue")
for i in range(3):
    turtle.color(boje[i])
    for j in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.right(120)
'''
