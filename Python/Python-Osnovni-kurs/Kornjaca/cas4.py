'''
ZADACI
'''

# Znak za štrikliranje
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas4#id13
'''
import turtle as t
t.color("blue")
t.width("5")
t.right(45)
t.forward(50)
t.left(90)
t.forward(100)
'''

# Kvadrat
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas4#id15
'''
import turtle
turtle.forward(100)   # иди напред 100 корака
turtle.left(90)       # окрени се 90 степени налево
turtle.forward(100)   # иди напред 100 корака
turtle.left(90)       # окрени се 90 степени налево
turtle.forward(100)   # иди напред 100 корака
turtle.left(90)       # окрени се 90 степени налево
turtle.forward(100)   # иди напред 100 корака
turtle.left(90)       # окрени се 90 степени налево
'''

# Kvadratni korijen
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas4#id17
'''
import turtle as t
t.color("red")
t.width("7")
t.speed(3)
t.forward(20)
t.right(60)
t.forward(100)
t.left(135)
t.forward(200)
t.right(75)
t.forward(70)
'''

# Logo petlje
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas4#id19
'''
import turtle
turtle.color("#18BC9C")
turtle.width(20)
turtle.right(45)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
'''

# PONAVLJANJE
# Kvadrat - petlja
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas4#id22
'''
import turtle
for i in range(4):        # ponovi 4 puta:
    turtle.forward(100)     #   idi napred 100 koraka
    turtle.left(90)        #   okreni se nalevo za 90 stepeni
'''

# Isprekidana linija
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas4#id24
'''
import turtle
for i in range(5):
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
'''

# Otisci kornjače
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas4#id26

# Bez petlje
'''
import turtle as t
t.penup()
t.stamp()
t.forward(30)
t.stamp()
t.forward(30)
t.stamp()
t.forward(30)
t.stamp()
t.forward(30)
t.stamp()
'''

# Sa petjom
'''
import turtle as t
t.penup()
for i in range(5):
    t.forward(30)
    t.stamp()
'''


# Pravilni mnogougao
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas4#id28
'''
import turtle
n = 6
for i in range(n):         # ponovi n puta:
    turtle.forward(100)        #   idi napred 100 koraka
    turtle.left(360/n)           #   okreni se za 360:n stepeni
'''

# Zvijezda
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas4#id30
'''

'''
