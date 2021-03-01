"""
Program po sadržaju sajta petlja.org
https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-karelzadaci

Dodatni zadaci
"""

# ZADACI
# Pomjeri sve loptice unazad
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-karelzadaci#id3
'''
from karel import *
while moze_napred():             # dok ima polja ispred Karela, ponavljaj
    napred();                        # idi napred
    while ima_loptica_na_polju():    # pokupi sve loptice sa polja
        uzmi()
    if ima_loptica_kod_sebe():
    	levo(); levo(); napred()        # idi jedno polje nazad
    while ima_loptica_kod_sebe():    # ostavi sve loptice
        ostavi()
    if ima_loptica_na_polju():
    	levo(); levo(); napred()         # vrati se jedno polje napred
'''

# Tri puta gore-dole
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-karelzadaci#id4
'''
from karel import *
for i in range(3):              # tri puta ponovi sve sto sledi
    napred(); levo()             #    udji u sledecu kolonu i okreni se na sever
    for i in range(4):
        napred()
    desno(); napred(); desno()   #    predji u sledecu kolonu i okreni se na jug
    for i in range(4):
        napred()
    levo()                       #    okreni se na istok
'''

# Gore-dole
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-karelzadaci#id5
'''
from karel import *
while moze_napred():
    napred(); levo()
    while moze_napred():
        napred()
    desno(); napred(); desno()
    while moze_napred():
        napred()
    levo()
'''

# Donesi sve sa table
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-karelzadaci#id6
'''
from karel import *
for i_kolona in range(4):      # cetiri puta ponovi ciscenje kolone
    napred()                   #     udji u sledecu kolonu
    levo()                     #     okreni se na sever
    for i in range(3):
        napred(); uzmi(); #     3 puta ponovi korak napred i uzimanje

    desno(); desno()           #     okreni se na jug
    for i in range(3):
        napred() #     3 koraka napred do donje ivice

    levo()                     #     okreni se na istok
    
                               # sada smo prosli sva polja
levo()                         #     okreni se na zapad
levo()
for i in range(4):
    napred() # vrati se na pocetno polje
    
for i_loptica in range(12):
    ostavi()
'''

# Donesi svih 60
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-karelzadaci#id7
'''
from karel import *
for i_kolona in range(4):      # cetiri puta ponovi ciscenje kolone
    napred()                   #     udji u sledecu kolonu
    levo()                     #     okreni se na sever
    for i in range(3):
        napred()
        for j in range(5):
            uzmi() #     3 puta ponovi korak napred i uzimanje

    desno(); desno()           #     okreni se na jug
    for i in range(3):
        napred() #     3 koraka napred do donje ivice

    levo()                     #     okreni se na istok
    
                               # sada smo prosli sva polja
levo()                         #     okreni se na zapad
levo()
for i in range(4):
    napred() # vrati se na pocetno polje
    
for i_loptica in range(60):
    ostavi()
'''

# Sakupi loptice na stepenicama
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-karelzadaci#id8
'''
from karel import *
for i in range(3):
    levo(); napred();
    while ima_loptica_na_polju():
        uzmi()
    desno(); napred();
    while ima_loptica_na_polju():
        uzmi()
for i in range(3):
    desno(); napred();
    while ima_loptica_na_polju():
        uzmi()
    levo(); napred();
    while ima_loptica_na_polju():
        uzmi()
'''

# Prepone
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-karelzadaci#id9
'''
from karel import *
while not ima_loptica_kod_sebe():
    levo()
    while moze_napred():
        napred()
    desno(); napred(); desno();
    while moze_napred():
        napred()
    if ima_loptica_na_polju():
        uzmi()
    levo()
'''
