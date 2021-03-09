'''
VJEŽBANJE
'''

# LINIJSKI PROGRAMI
# Slovo M
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas6#m
'''
import turtle

turtle.left(90)
turtle.forward(150)
turtle.right(150)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.right(150)
turtle.forward(150)
'''

# Dijamant
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas6#id6
'''
import turtle as t
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(60)
t.forward(100)
t.left(120)
t.forward(100)
'''

# PETLJE
# Kvadratni signal
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas6#id9
'''
import turtle
ugao = 90
duzina = 20

def napred_lijevo(d, u):
    turtle.forward(d)
    turtle.left(u)

def napred_desno(d, u):
    turtle.forward(d)
    turtle.right(u)

for i in range(5):
    napred_lijevo(duzina, ugao)
    napred_desno(duzina, ugao)
    napred_desno(duzina, ugao)
    napred_lijevo(duzina, ugao)
'''

# Testerica
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas6#id11
'''
import turtle, math

turtle.left(45)

for i in range(10):
    turtle.forward(25 * math.sqrt(2))
    turtle.right(135)
    turtle.forward(25)
    turtle.left(135)
'''

# Nasumično kretanje
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas6#id13
'''
import turtle, random
turtle.speed(0)
for i in range(100):
    turtle.forward(random.randint(20, 40)) # ispravi ovaj red
    turtle.left(random.randint(0, 360))                       # ispravi ovaj red
'''

# Nasumično kretanje - okreti u oba smjera
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas6#id15
'''
import turtle, random
turtle.speed(0)
for i in range(100):
    turtle.forward(random.randint(20, 40))
    ugao = random.randint(0, 360)
    if ugao < 180:               # ispravi ovaj red
        turtle.left(random.randint(0, 180))     # ispravi ovaj red
    else:
        turtle.right(random.randint(0, 360))    # ispravi ovaj red
'''

# Plus
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas6#id17
'''
import turtle
for i in range(4):
    turtle.forward(50)
    turtle.backward(50)
    turtle.right(90)
'''

# Osmokraka zvijezda
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas6#id19
'''
import turtle
for i in range(8):
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(45)
'''

# n-tokraka zvijezda
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas6#n
'''
import turtle
n = 150
a = 150
turtle.speed(0)
for i in range(n):
    turtle.forward(a)
    turtle.backward(a)
    turtle.left(360/n)
'''

# Parni i neparni krakovi različite dužine
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas6#id22
'''
import turtle
n = 150
a = 150
turtle.speed(0)

for i in range(n):
    if i % 2 == 0:
    	turtle.forward(a)
    	turtle.backward(a)
    else:
        turtle.forward(a-30)
        turtle.backward(a-30)
    turtle.left(360/n)
'''

# Slobodno crtanje
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas6#id24
'''
from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for broj in range(16):
        write(broj, align='center')
        right(90)
        for num in range(8):
                penup()
                forward(10)
                pendown()
                forward(10)
        penup()
        backward(160)
        left(90)
        forward(20)

torka = ("turtle", "red", "blue", "green", "orange")

ada = Turtle(); ada.color(torka[1]); ada.shape(torka[0])
ada.penup(); ada.goto(-160, 100); ada.pendown()
       
bob = Turtle(); bob.color(torka[2]); bob.shape(torka[0])
bob.penup(); bob.goto(-160, 70); bob.pendown()

ivy = Turtle(); ivy.color(torka[3]); ivy.shape(torka[0])
ivy.penup(); ivy.goto(-160, 40); ivy.pendown()

jim = Turtle(); jim.color(torka[4]); jim.shape(torka[0])
jim.penup(); jim.goto(-160, 10); jim.pendown()

for turn in range(30):
        ada.right(12)
        bob.right(12)
        ivy.right(12)
        jim.right(12)

for i in range(100):
        ada.forward(randint(1, 5))
        bob.forward(randint(1, 5))
        ivy.forward(randint(1, 5))
        jim.forward(randint(1, 5))
'''
