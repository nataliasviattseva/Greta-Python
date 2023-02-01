# ****************** #
## Lundi 30/01/2023 ##
# ****************** #

variable = 15


def portée_variable():
    print(variable)


def portée_variable2():
    global variable
    variable = 5


portée_variable2()

print(variable)
#
a = 3
print(f"a = 3, type(a): {type(a)}")

b = 5.3
print(f"b = 5.3, type(b): {type(b)}")

c = "Bonjour"
print(f'c = "Bonjour", type(c): {type(c)}')

d = (a > b)
print(f"d = (a > b), type(d): {type(d)}")

e = 6 / 3
print(f"e = 6 / 3, type(e): {type(e)}")

f = 6 // 3
print(f"f = 6 // 3, type(f): {type(f)}")

g = a + b
print(f"g = a + b , type(a): {type(a)}, type(b): {type(b)}, type(g): {type(g)}")

h = a + f       ## a = 3 (type: int), b = 5.3 (type: int)
print(f"h = a + f  , type(a): {type(a)}, type(f): {type(f)}, type(h): {type(h)}")

i = "3.14"
print(f'i = "3.14"  , type(i): {type(i)}')

j = float(i)
print(f'j = float(i) , type(j): {type(j)}')

# k = i + j # TypeError: can only concatenate str (not "float") to str
# print(type(j))

l = str(a)

m = str(f)

print(a, l, f, m, sep="***")
print("a + f =", a + f, "et l + m = ", l + m)

texte = "Salut \n tu vas bien ?"
print(texte)
print(texte, "texte")

prenom = input("Tapez votre prénom : ")
print("Vous vous appelez : ", prenom)

n = input("Donnez un nombre : ")
n = int(input("Donnez un nombre : "))
p = n + 7

q = float(input("Donnez un entier : "))
print(q)

r = int(input("Donnez un entier : "))
print(r)

s = int(3.14)
print(s)
print(type(s))

t = 8
print("t = 8")

u = "Truc"
print('u = "Truc"')

P = (t <= 10)
print("P = (t <= 10)")

Q = (u == "truc")
print('Q = (u == "truc")')

R = (u < "truc")
print('R = (u < "truc")')

print("P:", P)

print("Q:", Q)

print("R:", R)

print("P and Q:", P and Q)

print("P or Q:", P or Q)

print("P or R:", P or R)

print("not R:", not R)

print("P or (not R):", P or (not R))

print("P and (not R):", P and (not R))

print("(not P) and Q:", (not P) and Q)

print("not(P and Q):", not(P and Q))

# ********************* #
#  Marcredi 01/02/2023  #
# ********************* #
v = 37

w = 7

quotient = v // w
reste = v % w

print(v, "=", w, "x", quotient, "+", reste)

from math import *

x = 2.718
print(round(x, 2))
print(round(x**3.1))
print(abs(1 - x))
print(floor(x))
print(floor(1 - x))
print(floor(abs(1-x)))

print(round(exp(2), 3))
print(round(log(2), 2))
print(round(sqrt(2), 3))

print("Le", ord(chr(75)), "dans le ASCII équivalent à:", chr(75))
print("ASCCII code pour", chr(ord("È")), "est :", ord("È"))

texte = "Voici Henri"

# float(texte) # Error de formats
print("len(texte) :", len(texte))
print("texte.upper() :", texte.upper())
print("texte.lower() :", texte.lower())
print("texte[6] :", texte[6])
print("texte[7:8] :", texte[7:8])
print("texte[4:] :", texte[4:])
print("texte[:3] :", texte[:3])
print("texte[-3:] :", texte[-3:])
print("texte.find('i') :", texte.find('i')) # .find() trouve le premiere chaine dans le texte
print("texte.find('i', 5) :", texte.find('i', 5))
print("texte.find('i', 5, 9) :", texte.find('i', 5, 9))
print(type(texte.find('e', 5, 9)))

a = 1
b = a
a += 1
b += a
a += 1
b += a
a += 1
b += a

print(a)
print(b)

a = 1
b = a + 1
a = b + 2
b = a + 2
a = b + 3
b = a + 3

print(a)
print(b)

# {} en: braces fr: accolade

a = "mais"
b = "Non"
c = "allo"
d = "quoi"

message = "%s %s %s, %s !" % (b, a, c, d)
print(message)

message_format = "{} {} {}, {} !".format(b, a, c, d)
print(message_format)

message_f_string = f"{b} {a} {c}, {d} !"
print(message_f_string)

# découpage
e = message[4:13]
print(e)

e = message_format[4:13]
print(e)

e = message_f_string[4:13]
print(e)

animaux = ["girafe", "tigre", "singe", "souris"]
print(animaux)

tailles = [5, 2.5, 1.75, 0.15]
print(tailles)

mixte = ["girafe", 5, "souris", 0.15]
print(mixte)

print(animaux[0])
print(animaux[1])
print(animaux[3])

print([type(i) for i in animaux])

animaux_liste = f"animaux[0] = {animaux[0]}"
print(animaux_liste)

liste_formate = f"la liste formatée est :  {animaux}, {tailles}, {mixte}"
print(liste_formate)

# concatenation

ani1 = ["girafe", "tigre"]
ani2 = ["singe", "souris"]

animaux_complet = ani1 + ani2

print(f"ani1 + ani2 : {animaux_complet}")
print(f"ani1 * 3 : {ani1 * 3}")

# indexes négatives

print(animaux[-4])
print(animaux[-2])
print(animaux[-1])

toto = f"animaux[-4] = {animaux[-4]}, animaux[-2] = {animaux[-2]}, animaux[-1] = {animaux[-1]}"
print(toto)

print(f"animaux[0:2] : {animaux[0:2]}")
print(f"animaux[0:3] : {animaux[0:3]}")
print(f"animaux[0:] : {animaux[0:]}")
print(f"animaux[:] : {animaux[:]}")
print(f"animaux[1:] : {animaux[1:]}")
print(f"animaux[1:-1] : {animaux[1:-1]}")
print(f"animaux[::-1] : {animaux[::-1]}")

enclos1 = ["girafe", 4]
enclos2 = ["tigre", 2]
enclos3 = ["singe", 5]

zoo = [enclos1, enclos2, enclos3]
print(f"zoo : {zoo}")

print(f"zoo[1] : {zoo[1]}")
print(f"zoo[0][0] : {zoo[0][0]}")
print(f"zoo[0][1] : {zoo[0][1]}")
print(f"zoo[1][0] : {zoo[1][0]}")
print(f"zoo[1][1] : {zoo[1][1]}")
print(f"zoo[2][0] : {zoo[2][0]}")
print(f"zoo[2][0] : {zoo[2][1]}")

# 1
"""Constituez une liste 'semaine' contenant les 7 jours de la semaine. À partir de cette liste,
comment récupérez-vous seulement les 5 premiers jours de la semaine d'une part, et ceux du week-end
d'autre part (utlizer pour cela l'indiçage) ? Cherchez un autre moyen pour arriver au même résultat
(en utulusant un autre indiçage)."""

semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

print(semaine[0:5])
print(semaine[:5])
print(semaine[:-2])

print(semaine[5:7])
print(semaine[5:])
print(semaine[-2:])

# 2
"""Trouvez deux manières pour accéder au dernier jour de la semaine."""

print(semaine[6])
print(semaine[-1])

# 3
"""Inversez les jours de la semaine en une commande."""

# semaine.reverse()
# print(semaine)
print(semaine[::-1])

# 4
"""Créez 4 listes 'hiver', 'printemps', 'été' et 'automne' contenant les nois correspondant à ces saisons.
Créez ensuite une liste 'saisons' contenant les sous-listes 'hiver', 'printemps', 'été' et 'automne'. 
Prévoyez ce que valent les variables suivantes, puis vérifiez-le dans l'interpéteur:
- saisons[2]
- saisons[1][0]
- saisons[1:2]
- saisons[:][1]
Comment expliquez-vouz ce dernier résultat ?"""

hiver = ["Décembre", "Janvier", "Février"]
printemps = ["Mars", "Avril", "May"]
ete = ["Juin", "Juillet", "Août"]
automne = ["Septembre", "Octobre", "Novembre"]

saisons = [hiver, printemps, ete, automne]

print(f"saisons[2] : {saisons[2]}")
print(f"saisons[1][0] : {saisons[1][0]}")
print(f"saisons[1:2] : {saisons[1:2]}")
print(f"saisons[:][1] : {saisons[:][1]}")

# 5
"""Affichez la table des 9 en une seule commande avec l'instructon range()"""

[print(f"{i} x 9 = {i * 9}") for i in range(1, 10)]

# 6
"""Avec Python, répondez à la question suivante en une seule commande. Combien y a-t-il de nombres
pairs dans l'intervale [2, 10000] inclus ?"""

# option 1 : utilizer le 'counter', condition '%2' et liste en compréhension
compteur1 = 0
print(f"option 1 : {sum([compteur1+1 for i in range(1, 10001) if i% 2 == 0])}")

# option 2 : utilizer le 'counter', condition '%2' et circle 'for'
compteur2 = 0
for i in range(2, 10001):
    if i % 2 == 0:
        compteur2 += 1
print(f"option 2 : {compteur2}")

# option 3 : modification de variante 2 - utiliser le 'step' de founction range()
compteur3 = 0
for i in range(2, 10001, 2):
    compteur3 += 1
print(f"option 3 : {compteur3}")

# option 4 (pas préferable) : utiliser les founctions len() et range()
print(f"option 4 : {len(range(2, 10001, 2))}")

# option 5 (pas le mien) :
## la boucle va créer une liste des reste des divisions par 2 de tous les éléments du range.
## Les nombres pairs auront un reste & 0, les impairs un reste à 1
## [0, 1, 0, 1, 0 ...]
## la méthode .count(0) va compter le nombre d'éléments 0 dans la liste (soit le nombre de nombres pairs)
print(f"option 5 : {([i % 2 for i in range(2, 10001)]).count(0)}")
