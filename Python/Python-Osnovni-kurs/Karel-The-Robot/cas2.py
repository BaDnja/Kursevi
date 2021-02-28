"""
Program po sadržaju sajta petlja.org
https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas2

Drugi čas
----------------------
- Uslovne petlje, grananje
- Ponavljanje - uslovna petlja while
- Grananje
- Domaći zadatak
"""

'''
Uslovne petlje - grananje

moze_napred() - provjerava da li se robot može pomjeriti napred (da li ispred njega postoji zid),
ima_loptica_na_polju() - provjerava da li na polju na kojem se robot nalazi ima loptica,
broj_loptica_na_polju() - vraća broj loptica na polju na kojem se robot nalazi,
ima_loptica_kod_sebe() - provjerava da li robot trenutno ima loptica kod sebe,
broj_loptica_kod_sebe() - vraća broj loptica koje robot trenutno ima kod sebe.
'''

# Ponavljanje - uslovna petlja while
# Idi napred dok možeš
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas2#id2
'''
from karel import *
while mozeNapred():
    napred()
uzmi()
'''

# Kupi loptice dok možeš
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas2#id5
'''
from karel import *
napred()
for i in range(broj_loptica_na_polju()):
    uzmi()
'''

# Grananje
# Pokupi lopticu ako je ima
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas2#id9
'''
from karel import *
napred();             # idi napred
if ima_loptica_na_polju():  # ako je na polju loptica:
    uzmi()       #    uzmi lopticu

napred();             # idi napred
if ima_loptica_na_polju():  # ako je na polju loptica:
    uzmi()       #    uzmi lopticu

napred();             # idi napred
if ima_loptica_na_polju():  # ako je na polju loptica:
    uzmi()
'''

# Sa for petljom
'''
from karel import *
for i in range(3):
    napred()
    if ima_loptica_na_polju():
        uzmi()
'''

# Sa while petljom
'''
from karel import *
while moze_napred():
    napred()
    if ima_loptica_na_polju():
        uzmi()
'''

# ZADATAK: Uzimanje i ostavljanje loptica
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas2#id14
'''
from karel import *
for i in range(3):
    napred()
    if ima_loptica_na_polju():
        uzmi()
    else:
        ostavi()
'''

# ZADATAK: Kretanje u krug
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas2#id16
'''
from karel import *
for i in range(4):
    while moze_napred():
        napred()
        if ima_loptica_na_polju():
            uzmi()
    levo()
'''

# Rješenje koristeći for petlju
'''
from karel import *
for i in range(20):
    if moze_napred():
        napred()
        if ima_loptica_na_polju():
            uzmi()
    else:
        levo()
'''

# DOMAĆI ZADATAK
# ZADATAK: Loptice na tri strane
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas2#id20
'''
from karel import *
for i in range(3):
    while moze_napred():
        napred()
        uzmi()
    levo()
'''

# ZADATAK: Pokupi loptice do kojih možeš da dođeš
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas2#id23
# NAPOMENA: Lavirint se nasumično kreira
'''
from karel import *
while moze_napred():
    napred()
    # okreni se prema jugu
    desno()
    # proveri da li je prepreka ispred tebe
    if moze_napred():
        # idi po lopticu
        napred()
        uzmi()
        # vrati se nazad
        levo()
        levo()
        napred()
        desno()
    else:
        # okreni se prema istoku
        levo()
'''
