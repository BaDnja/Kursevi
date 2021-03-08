
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
import turtle
m = 20
n = 3
turtle.speed(0)
for i in range(m):
    turtle.color("red")
    for j in range(n):
        turtle.forward(60)
        turtle.left(120)
    turtle.color("black")
    turtle.forward(10)
    turtle.left(18)
'''

# Deset kvadrata
'''
import turtle
a = 10
turtle.speed(6)
turtle.width(2)
for i in range(10):
    for j in range(4):
        turtle.forward(a)
        turtle.left(90)
    a = a + 10
'''

# PROCEDURE
# Procedura za crtanje mnogougla
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas5#id15
'''
# procedura za crtanje pravilnog poligona
# parametri su broj stranica poligona n i duzina stranice a
def poligon(n, a):
    for i in range(n):             # n puta ponovi:
        turtle.forward(a)          #    idi napred a koraka
        turtle.right(360 / n)      #    okreni se za spoljasnji ugao n-tostranog pravilnog poligona
'''

# Četiri kvadrata
'''
import turtle
ugao = 90

def kvadrat(n):
    for i in range(4):
        turtle.forward(n)
        turtle.left(90)

def cetiri_kvadrata(angle):
    for i in range(4):
        kvadrat(100)
        turtle.left(angle)
        
cetiri_kvadrata(ugao)
'''

# TORKE/LISTE
# Šareni kvadrat - petlja
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas5#id24
'''
import turtle
boje = ("red", "green", "", "yellow")
for i in range(4):      # ponovi 4 puta:
    turtle.color(boje[i])    #   postavi boju na i-ti element torke boja
    turtle.forward(100)     #   idi napred 100 koraka
    turtle.left(90)        #   okreni se nalevo za 90 stepeni
'''

# Zvijezda bez presijecanja
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas5#id26
'''
import turtle
uglovi = (72, -144)
for i in range(10):          # ponovi 10 puta:
    turtle.forward(40)         #    idi napred 40 koraka
    if i % 2 == 0:
    	turtle.left(uglovi[0])     #    okreni se ulevo za naredni od dva ugla iz liste
    else:
        turtle.left(uglovi[1])
'''

# Domaći zadatak
# Šareni oblik
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas5#id29
'''
import turtle

turtle.speed(0)
turtle.width(5)
for i in range(120):
    if i % 3 == 0:
        turtle.color("red")
        turtle.forward(50)
        turtle.left(31)
        turtle.color("green")
        turtle.forward(70)
        turtle.left(71)
        turtle.color("blue")
        turtle.forward(90)
        turtle.left(101)
'''

# Kvadrat šarenih ivica
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/kornjaca-cas5#id31
'''
import turtle

turtle.width(10)

def sarena_duz(n, a, boja1, boja2):
    for i in range(n):
        if i % 2 == 0:
            turtle.color(boja1)
        else:
            turtle.color(boja2)
        turtle.forward(a)


sarena_duz(11, 10, "red", "blue")
turtle.left(90)
sarena_duz(11, 10, "yellow", "green")
turtle.left(90)
sarena_duz(11, 10, "purple", "orange")
turtle.left(90)
sarena_duz(11, 10, "black", "green")
turtle.left(90)
'''


