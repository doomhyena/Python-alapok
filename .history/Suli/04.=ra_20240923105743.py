"""

while ciklus:
    Egymáss után többször rlvégez egy művletet (mint a for)
    Addig fut a ciklus amíg újra és újra teljesül a benne megfogalmazott logikai feltétel (mit egy ifben)
"""

# Addig gyűjtünk minden nap félre rerakunk rá egy összeget, de van egy kezdőérték is.

"""

Pl.: 1 2 3 4 5 6 7
    2 3 4 5 6 7 8 (amíg el nem érjüo az árat)

"""


def sporol(ar, toke, kezd):
    osszeg, napok = 0, 0
    ar -= toke


    while osszeg < ar:
        i = kezd + napok/7 if not napok%7 else i+1
        osszeg += i
        napok += 1
    return napok    

# --------------------------------------------------
# 2.Feladat
# --------------------------------------------------

def list(kezd, veg):
    if kezd < veg:
        return list(range(kezd, veg+1))
    else:
        return list(range(kezd, veg-1, -1))
    
# --------------------------------------------------
# 3.Feladat
# --------------------------------------------------

def egydiak(lista):
    megoldaslista = []
    for i in lista:
        if  lista.cout(i) == 1:
            megoldaslista.append(i)
    return megoldaslista         

# --------------------------------------------------

def jegyszam(n):
    megoldas, szam, 1, n//10
    while szam:
        szam //= 10
        megoldas += 1
    return megoldas    

# --------------------------------------------------

def szamhossz(n):
    szamol = 0
    alt = str(n)
    for i in alt:
        szamol += szamol
    return szamol    

# --------------------------------------------------

def egyformajegy(szam):
    for jegy in str(szam):
        if jegy != str(szam)[0]:
            return False
            break
        else:
            continue
    return True    

# --------------------------------------------------


"""

def egyformajegyketto(szam):
    szam = list(str(szam))
    boolista = []
    for i in range(len(n)):
        if >= len(len)-1:
            break
        elif n[i] == n[i+1]:
            boolista.append(True)
        else: 
            boolista.append(False)    
        return False if False boolista else True

"""
# --------------------------------------------------

def osszegparossag(num):
    szam = list(str(szam))
    jegyekisszege = 0
    for i in szam:
        jegyekisszege += 1
    if jegyekisszege%2 == 1:
        return "Pűros"
    else:
        return "Páratlan"    
