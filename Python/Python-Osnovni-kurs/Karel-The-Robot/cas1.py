"""
Program po sadržaju sajta petlja.org
https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas1

Prvi čas
----------------------
- Naredbe koje Karel razumije
- Linijski programi
- Ponavljanje - Brojačka petlja for
- Domaći zadatak
"""

"""
Naredbe koje Karel razumije

napred() - pomjeri se jedno polje napred,
levo() - okreni se za 90 stepeni nalijevo (u smjeru suprotnom kazaljki na satu),
desno() - okreni se za 90 stepeni nadesno (u smjeru kazaljke na satu),
uzmi() - pokupi lopticu sa polja na kojem se nalaziš,
ostavi() - spusti lopticu na polje na kojem se nalaziš
"""

# LINIJSKI PROGRAMI

# ZADATAK: Idi do loptice i uzmi je
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas1#id4

# from karel import *
# napred()      # idi napred
# napred()      # idi napred
# levo()        # okreni se nalijevo
# napred()      # idi napred
# napred()      # idi napred
# uzmi()        # uzmi lopticu

# Prikaz sintaksnih grešaka
# ZADATAK: sa greškama:
'''
from karel import *
napred()
napred
  levo()
napred)
    napred[]
 uzmi{}
'''
# Rješenje
'''
from karel import *
napred()
napred()
levo()
napred()
napred()
uzmi()
'''

# Kucanje naredbi u jednoj liniji (obavezan znak ;)
'''
from karel import *
napred(); napred(); levo(); napred(); napred(); uzmi()'''

# ZADATAK: Programiranje slaganjem blokova (Blockly)
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas1#id8

'''
from karel import * 
napred()
napred()
levo()
napred()
napred()
uzmi()
'''

# ZADATAK: Prebaci lopticu na polje (3, 5)
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas1#id9
'''
from karel import *
napred()
napred()
levo()
napred()
napred()
desno()
napred()
uzmi()
napred()
levo()
napred()
napred()
levo()
napred()
napred()
ostavi()
'''

# ZADATAK: Prebaci obe loptice u rupu
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas1#id11
'''
from karel import *
desno(); napred(); napred();
uzmi();
desno(); desno(); napred(); levo(); napred();
ostavi();
napred(); levo(); napred(); uzmi();
desno(); desno(); napred(); desno(); napred();
ostavi()
'''

# PONAVLJANJE - BROJAČKA PETLJA FOR
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas1#id13

'''
from karel import *
napred()
napred()
napred()
napred()
napred()
napred()
napred()
napred()
uzmi()
'''
# Korištenjem petje for
'''
from karel import *
for i in range(8):
    napred()
uzmi()'''

# Neke česte greške
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas1#id16

# Pogrešno rješenje
'''
from karel import *
for i in range(8)
napred()
 uzmi()
'''

# Ispravno rješenje
'''
from karel import *
for i in range(8):
	napred()
uzmi()
'''

# ZADATAK: Pokupi 10 loptica
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas1#id22
'''
from karel import *
napred()
for i in range(10):
    uzmi()
'''

# ZADATAK: Pokupi pet loptica na pet polja ispred
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas1#id24
'''
from karel import *
for i in range(5):
    napred()
    uzmi()
'''
# Uzmi pet lopti na pet polja ispred, i vrati se nazad
'''
from karel import *
for i in range(5):
    napred()
    uzmi()
desno(); desno();
for i in range(5):
    napred()
'''
# Ostavi lopte na isto mjesto pri povratku nazad
'''
from karel import *
for i in range(5):
    napred()
    uzmi()
desno(); desno()
for i in range(5):
    ostavi()
    napred()
'''

# ZADATAK: Pokupi po tri loptice na pet polja ispred (ugnježdena petlja)
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas1#id28
'''
from karel import *
for i in range(5):
    napred()
    for j in range(3):
        uzmi()
'''

# DOMAĆI ZADATAK
# ZADATAK: Prebaci obe loptice u rupu
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas1#id31
'''
from karel import *
for i in range(2):
    napred()
levo()
for i in range(2):
    napred()
uzmi(); desno();
for i in range(2):
    napred()
levo(); napred(); uzmi(); napred(); levo();
for i in range(4):
    napred()
for i in range(2):
    ostavi()
'''

# ZADATAK: Razmaknute loptice
# https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas1#id34
'''
from karel import *
for i in range(3):
    napred(); napred();
    uzmi()
'''
