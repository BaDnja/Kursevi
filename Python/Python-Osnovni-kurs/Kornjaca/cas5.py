
# Isprekidana linija
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas5#id4
'''
import turtle
for i in range(10):
    turtle.forward(20)
    if i%2==0:
        turtle.penup()
    else:
        turtle.pendown()
'''

# Zvijezda bez presijecanja
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas5#id6
'''
import turtle
for i in range(10):        # ponovi 10 puta:
    turtle.forward(40)     #    idi napred 40 koraka
    if i%2==0:                #    ako je vrednost brojaca i paran broj:
        turtle.left(72)         #       okrneni se ulevo za 72 stepena
    else:                  #    u suprotnom:
        turtle.right(144)         #       okreni se udesno za 144 stepena
'''

# Ugnježdene petlje
# Tri kvadrata
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas5#id9
'''
import turtle

for i in range(3):
    for j in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.right(120)
'''

# Komplikovanija zvijezda
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas5#id11
'''

'''
