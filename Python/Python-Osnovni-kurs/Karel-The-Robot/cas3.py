"""
Program po sadržaju sajta petlja.org
https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas3

Treći čas - Vježbanje
----------------------
- Petlja for
- Petlja while
- Grananje
- Ugnježdene petlje
"""

# PETLJA FOR
# Prebaci pet loptica u rupu
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas3#id2
'''
from karel import *
napred()
for i in range(5):
    uzmi()
napred()
for i in range(5):
    ostavi()
'''

# Pokupi loptice sa naredna tri polja
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas3#id5
'''
from karel import *
napred()
for i in range(5):
    uzmi()
napred()
for i in range(3):
    uzmi()
napred()
for i in range(8):
    uzmi()
'''

# Pobjedničko postolje
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas3#id6
'''
from karel import *
for i in range(5):
    levo()
    napred()
    desno()
    napred()
    uzmi()
for i in range(5):
    napred()
    desno()
    napred()
    uzmi()
    levo()
'''

# PETLJA WHILE
# Stepenice
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas3#id9
'''
from karel import *
while moze_napred():
    napred()
    desno()
    napred()
    uzmi()
    levo()
'''

# GRANANJE
# Donesi sve loptice
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas3#id13
'''
from karel import *
while moze_napred():
    napred()
    if ima_loptica_na_polju():
        uzmi()

levo(); levo()                # okreni se nazad
while moze_napred():
    napred()

while ima_loptica_kod_sebe(): # ostavi sve loptice
    ostavi()
'''

# UGNJEŽDENE PETLJE
# Premjesti sve loptice u rupe (3x3)
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas3#x3
'''
from karel import *
while moze_napred():
    napred()
    while ima_loptica_na_polju():
        uzmi()
    napred()
    while ima_loptica_kod_sebe():
        ostavi()
'''

# Prebaci sve loptice u rupe
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas3#id17
'''
from karel import *
while moze_napred():
    napred()
    while ima_loptica_na_polju():
        uzmi()
    napred()
    while ima_loptica_kod_sebe():
        ostavi()
'''

# Uzimaj po četiri loptice do kraja
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas3#id20
'''
from karel import *
while moze_napred():
    napred()
    while ima_loptica_na_polju():
        uzmi()
'''

# Pokupi sve loptice
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas3#id21
'''
from karel import *
while moze_napred():
    napred()
    while ima_loptica_na_polju():
        uzmi()
'''

# Pun lavirint loptica
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas3#id22
'''
from karel import *
from karel import *
for i in range(4):
    while moze_napred():
        napred()
        ostavi()
    desno()
'''


