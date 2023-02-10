# ****************** #
## Lundi 06/02/2023 ##
# ****************** #

def si_len_matrices_egal(mat_a, mat_b):
    """Si la dimentions sont identiques"""
    if len(mat_a) == len(mat_b) and len(mat_a[0]) == len(mat_b[0]):
        return True
    else:
        return False


# option 1 possible mais pas ajustable
def addition(mat_a, mat_b):
    """Addition les deux matrices le même dimenton"""
    matrice_final = [[0]*len(mat_a[0]) for i in range(len(mat_a))]
    for i in range(0, len(mat_b)):
        for j in range(0, len(mat_a[i])):
            matrice_final[i][j] = mat_a[i][j] + mat_b[i][j]
    return matrice_final


def addition_1(mat_a, mat_b):
    """Addition les deux matrices le même dimenton"""
    if si_len_matrices_egal(mat_a, mat_b):
        matrice_final = []
        for i in range(0, len(mat_a)):
            tmp = []
            for j in range(0, len(mat_a[i])):
                tmp.append(mat_a[i][j] + mat_b[i][j])
            matrice_final.append(tmp)
        return matrice_final
    else:
        return "Les dimention des matrices sont differents."


def multiplication_par_scalaire(mat, number):
    """Multiplication d'une matrice par un scalaire"""
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            mat[i][j] *= number
    return mat

def multiplication_par_scalaire_1(mat, number):
    """Multiplication d'une matrice par un scalaire"""
    matrice_final = []
    for i in range(0, len(mat)):
        tmp = []
        for j in range(0, len(mat[i])):
            tmp.append(mat[i][j] * number)
        matrice_final.append(tmp)
    return matrice_final


def transition_matrice(mat):
    """Colonnes devient de lignes, lignes devient les colonnes"""
    trans_mat = []
    for i in range(len(mat[0])):
        tmp = []
        for j in range(len(mat)):
            tmp.append(mat[j][i])
        trans_mat.append(tmp)
    return trans_mat


def verifier_matrices_pour_multiplication(mat1, mat2):
    if len(mat1[0]) == len(mat2):
        return True
    else:
        return False


def multiplication_matrices(mat_a, mat_b):
    matrice_final = [[0, 0], [0, 0]]
    if verifier_matrices_pour_multiplication(mat_a, mat_b):
        for i in range(0, len(mat_a)):
            for j in range(0, len(mat_a[0])):
                for k in range(0, len(mat_a[0])):
                    matrice_final[i][j] += mat_a[i][k]*mat_b[k][j]
        return matrice_final
    else:
        return "Ce n'est pas possible de multiplier les matrices"


def multiplication_matrices_1(mat_a, mat_b):
    """Retourne la multiplication de matrices"""
    matrice_final = []
    if verifier_matrices_pour_multiplication(mat_a, mat_b):
        for i in range(0, len(mat_a)):
            tmp = []
            for j in range(0, len(mat_a[0])):
                total = 0
                for k in range(0, len(mat_a[0])):
                    total += mat_a[i][k]*mat_b[k][j]
                    # print(f"mat_a[{i}][{k}] = {mat_a[i][k]}")
                    # print(f"mat_b[{k}][{j}] = {mat_b[k][j]}")
                    # print(f"total = {total}")
                tmp.append(total)
                # print(f"tmp: {tmp}")
            matrice_final.append(tmp)
            # print(f"matrice_final: {matrice_final}")
        return matrice_final
    else:
        return "Ce n'est pas possible de multiplier les matrices"


matrice_a = [[2, 3], [4, 2], [1, 0]]
matrice_b = [[1, 2], [0, 1], [1, 4]]

print(addition_1(matrice_a, matrice_b))

matrice = [[2, 3], [4, 2], [1, 0]]
print(multiplication_par_scalaire(matrice, 3))

print(transition_matrice(matrice))

mat_c, mat_d = [[2, 1], [1, 4]], [[-4, 2], [0, 2]]
print(multiplication_matrices_1(mat_c, mat_d))
print(multiplication_matrices_1(mat_d, mat_c))


def verifier_que_matrice_carre(matrice):
    if len(matrice) == len(matrice[0]) == 2:
        return True
    else:
        return False


def calcul_determinant_matrice_carre(matrice):
    if verifier_que_matrice_carre(matrice):
        determinant = matrice_2_2[0][0] * matrice_2_2[1][1] - matrice_2_2[1][0] * matrice_2_2[0][1]
    else:
        determinant = 0
    return determinant


def calcul_inversion_matrice_carre(matrice):
    det = calcul_determinant_matrice_carre(matrice)
    if det != 0:
        # Transposition de deux valeurs
        tmp = matrice[0][0]
        matrice[0][0] = matrice[1][1]
        matrice[1][1] = tmp

        matrice[0][1] *= -1
        matrice[1][0] *= -1

        mati = []
        for ligne in matrice:
            matj = []
            for element in ligne:
                matj.append(element * (1 / det))
            mati.append(matj)
        return mati
    else:
        print("Opération impossible. Le determinant est égale zero.")
        return None


def matrice_inversible(matrice):
    if calcul_determinant_matrice_carre(matrice) != 0:
        return True
    else:
        return False


def determiner_adjoint_matrice(matrice):
    if matrice_inversible(matrice):
        a = matrice[0][0]
        b = matrice[0][1]
        c = matrice[1][0]
        d = matrice[1][1]
        return [[d, (-1)*b], [(-1)*c, a]]
    else:
        return "pas ajustible"


matrice_2_2 = [[2, 5], [3, 7]]
print(f"Calcul le detrminant de matrice carré : \n{calcul_determinant_matrice_carre(matrice_2_2)}")
print(f"Adjoint de matrice carré : \n{determiner_adjoint_matrice(matrice_2_2)}")
print(f"Calcul l'inversion de matrice carré : \n{calcul_inversion_matrice_carre(matrice_2_2)}")

# ****************** #
## Mardi 07/02/2023 ##
# ****************** #

def elimin_lin_col(m, n, matrice_muneur):
    # Retourne la matrice matrice_mineur sans la m-ième ligne et la n-ième colonne
    matrice_mineur_lin = len(matrice_muneur)
    result = []
    rep = []
    for i in range(matrice_mineur_lin):
        if i != m:
            for j in range(matrice_mineur_lin):
                if j != n:
                    result.append(matrice_muneur[i][j])
    for k in range(0, len(result), matrice_mineur_lin - 1):
        rep.append(result[k:k + matrice_mineur_lin - 1])
    return rep


matrice_3_3 = [[1, 1, 4], [2, -1, 3], [-2, 4, 3]]

print(elimin_lin_col(1, 1, matrice_3_3))


from tkinter import *
from random import *


def NouveauLance():
    nb = randint(1, 6)
    Texte.set('Resultat ->' + str(nb))


def ClickButton():
    Texte.set('BLABLA')


# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('Dé à 6 faces')

# Création d'un widget Button (bouton lancer)
BoutonLancer = Button(Mafenetre, text="Lancer")
# BoutonLancer = Button(Mafenetre, text="Lancer", command=NouveauLance)

# Positionnement du widjet avec la métode pack()
BoutonLancer.pack(side=LEFT, padx=10, pady=10)

BoutonMoi = Button(Mafenetre, text="Click me", command=ClickButton)
BoutonMoi.pack(side=LEFT, padx=15, pady=15)

# Création d'un widget Button (bouton Quitter)
BoutonQuitter = Button(Mafenetre, text="Quitter", command=Mafenetre.destroy)
BoutonQuitter.pack(side=LEFT, padx=15, pady=15)

Texte = StringVar()

# On appelle une fois la founction pout initialiser notre Texte
NouveauLance()

# Création d'un widget label (texte 'Resultat -> x')
LabelResult = Label(Mafenetre, textvariable=Texte, fg='red', bg='white')
LabelResult.pack(side=LEFT, padx=5, pady=5)

Mafenetre.mainloop()

# ********************* #
## Vendredi 10/02/2023 ##
# ********************* #

dictionnaire_list = [["Ambulance", "Krankenwagen"], ["Hôpital", "Krankenhaus"], ["Infirmière", "Krankenschwester"]]

for i, element in enumerate(dictionnaire_list):
    if "Hôpital" in dictionnaire_list[i]:
        print(dictionnaire_list[i][1])
# resultat: Krankenhaus

def traduction(mot):
    global dictionnaire_list
    for element in dictionnaire_list:
        if element[0] == mot:
            return element[1]
    return "pas trouve"


# Tests pour def traduction
print("\nTests pour def traduction:")
print(traduction("Hôpital"))
print(traduction("Ambulance"))
print(traduction("aaa"))
# resultat:
# Tests pour def traduction_for_for:
# Krankenhaus
# Krankenwagen
# pas trouve


def traduction_enumerate(mot):
    for i, j in enumerate(dictionnaire_list):
        if mot in dictionnaire_list[i]:
            return dictionnaire_list[i][1]
    return "pas trouve"


# Tests pour def traduction_enumerate
print("\nTests pour def traduction_enumerate:")
print(traduction_enumerate("Hôpital"))
print(traduction_enumerate("Ambulance"))
print(traduction_enumerate("aaa"))
# resultat:
# Tests pour def traduction_for_for:
# Krankenhaus
# Krankenwagen
# pas trouve


def traduction_for_for(mot):
    for i in dictionnaire_list:
        for j in i:
            if mot in i:
                return i[1]
    return "pas trouve"


# Tests pour def traduction_enumerate
print("\nTests pour def traduction_for_for:")
print(traduction_for_for("Hôpital"))
print(traduction_for_for("Ambulance"))
print(traduction_for_for("aaa"))
# resultat:
# Tests pour def traduction_for_for:
# Krankenhaus
# Krankenwagen
# pas trouve

# création de dictionnaire
dictionnaire = {}  # dictionnaire vide
capitales = {"France": "Paris", "Allemagne": "Berlin"}

# Outre manière de creation dictionnaire (list de tuples transforme en dict)
liste_capitales = [("France", "Paris"), ("Allemagne", "Berlin")]
capitales_1 = dict(liste_capitales)
print(capitales_1)
# resultat: {'France': 'Paris', 'Allemagne': 'Berlin'}

# affichage avec le même clé
capitales_changes= {"France": "Paris", "Allemagne": "Berlin", "France": "Marceille"}
print(capitales_changes)
# resultat: {'France': 'Marceille', 'Allemagne': 'Berlin'}

# ajouter element dans le dictionnaire
capitales["Islande"] = "Reykjavik"
print(capitales)
# resultat: {'France': 'Paris', 'Allemagne': 'Berlin', 'Islande': 'Reykjavik'}

# acceder à une valeur
result = capitales["Allemagne"]
print(result)
# resultat: Berlin

# result = capitales["Syldavie"]
# print(result)
# resultat: KeyError: 'Syldavie'

# get() avec 2 arguments: la clé et le résultat renvoyé au cas où la clé serait absente
result = capitales.get("Syldavie", "non resolu")
print(result)
# resultat: non resolu

result = capitales.get("Allemagne", "non resolu")
print(result)
# resultat: Berlin

if "Islande" in capitales:
    print(capitales["Islande"])
# resultat: Reykjavik

if "Reykjavik" in capitales:
    print("Test d'appartanance réussi")
else:
    print("Cette clé est absente du dictionnaire")
# resultat: Cette clé est absente du dictionnaire

# mettre à jour une valeur
capitales["France"] = "Marseille"
print(capitales)
# resultat: {'France': 'Marseille', 'Allemagne': 'Berlin', 'Islande': 'Reykjavik'}

# utiliser un tupple comme le clé
coords = {("Paris", "France"): ["48º51‘N", "22º1‘E"], ("Berlin", "Allemande"): ["52º31‘N", "13º24‘O"]}
result = coords[("Paris", "France")]
print(result)
# resultat: ['48º51‘N', '22º1‘E']

# supprimer un élément
del capitales["Allemagne"]
print(capitales)
# resultat: {'France': 'Paris', 'Islande': 'Reykjavik'}

# attention pour pas supprimer le dictionaire
# del capitales
# print(capitales)
# resultat: NameError: name 'capitales' is not defined

# fonction len()
capitales = {'France': 'Paris', 'Allemagne': 'Berlin', 'Islande': 'Reykjavik'}
print(len(capitales))
# resultat: 3

# dict.clear() supprime tous les éléments d'un dictionnaire. En clair, il le vide.
capitales.clear()
print(capitales)
# resultat: {}

# dict.items() retourne toutes les paires clé-valeur sous la forme d'une liste de tuples
capitales = {'France': 'Paris', 'Allemagne': 'Berlin', 'Islande': 'Reykjavik'}
result = capitales.items()
print(result)
# resultat: dict_items([('France', 'Paris'), ('Allemagne', 'Berlin'), ('Islande', 'Reykjavik')])

# dict.keys() retourne toutes les clés du dictionnaire sous la forme d'une liste
result = capitales.keys()
print(result)
# resultat: dict_keys(['France', 'Allemagne', 'Islande'])

# dict.values() retourne toutes les valeurs du dictionnaire sous la forme d'une liste
result = capitales.values()
print(result)
# resultat: dict_values(['Paris', 'Berlin', 'Reykjavik'])
