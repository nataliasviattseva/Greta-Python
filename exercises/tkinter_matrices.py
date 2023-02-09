from tkinter import *

COLOR_1 = "#6096B4"
COLOR_2 = "#93BFCF"
COLOR_3 = "#BDCDD6"
COLOR_4 = "#EEE9DA"

SIZE = "500x600"
WIDTH_PRAME_FIRST_LEVEL = 490


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


def calcul_determinant_matrice_de_2():
    matrice = []
    idx = 0

    for i in input_matrice_1.get("1.0", END).splitlines():
        if i != '':
            matrice.append([])
            for j in i.split(","):
                if j.lstrip("-").isnumeric():
                    matrice[idx].append((int(j)))
            idx += 1
    print(matrice)
    num = matrice[0][0] * matrice[1][1] - matrice[0][1] * matrice[1][0]
    print(f"num={num}")

    text_result.insert(END, num)

    return num


# Création de la fenêtre principale (main window)
fenetre = Tk()
fenetre.title('Calcul de matrices')
fenetre.geometry(SIZE)
fenetre.config(bg=COLOR_1)

# ---------- Première frame (Input frame) ---------- #
frame_1 = Frame(fenetre, width=WIDTH_PRAME_FIRST_LEVEL, height=180, bg=COLOR_2)
frame_1.pack(pady=5)
frame_1.propagate(False)

# ---------- Frame pour matrice 1 ---------- #
frame_1_1 = Frame(frame_1, width=220, height=160, bg=COLOR_3)
frame_1_1.pack(side=LEFT, padx=10, pady=10)
frame_1_1.propagate(False)

# ---------- Text input pour matrice 1 ---------- #
input_matrice_1 = Text(frame_1_1, width=200, height=140, bg=COLOR_4)
input_matrice_1.pack(padx=10, pady=10)

# ---------- Frame pour matrice 2 ---------- #
frame_1_2 = Frame(frame_1, width=220, height=160, bg=COLOR_3)
frame_1_2.pack(side=LEFT, padx=10, pady=10)
frame_1_1.propagate(False)

# ---------- Text input pour matrice 2 ---------- #
input_matrice_2 = Text(frame_1_2, width=200, height=140, bg=COLOR_4)
input_matrice_2.pack(padx=10, pady=10)

# ---------- Deuxère frame (Boutons frame) ---------- #
frame_2 = Frame(fenetre, width=WIDTH_PRAME_FIRST_LEVEL, height=180, bg=COLOR_2)
frame_2.pack(pady=5)
frame_2.propagate(False)

# ---------- Frame pour les boutons founctionels ---------- #
frame_2_1 = Frame(frame_2, width=220, height=170, bg=COLOR_3)
frame_2_1.pack(side=LEFT, padx=5, pady=5)
frame_2_1.propagate(False)

bouton_addition_matrices = Button(frame_2_1, text="Addition Matrices")
bouton_addition_matrices.pack(anchor=NW, padx=10, pady=4, fill=BOTH)
#
bouton_multiplication_scalaire = Button(frame_2_1, text="Multiplication Scalaire")
bouton_multiplication_scalaire.pack(padx=10, pady=4, fill=BOTH)
#
bouton_transition = Button(frame_2_1, text="Transition")
bouton_transition.pack(padx=10, pady=4, fill=BOTH)

bouton_multiplication_matrices = Button(frame_2_1, text="Multiplication Matrices")
bouton_multiplication_matrices.pack(padx=10, pady=4, fill=BOTH)

bouton_invertion = Button(frame_2_1, text="Invertion", command=calcul_determinant_matrice_de_2)
bouton_invertion.pack(padx=10, pady=4, fill=BOTH)

bouton_quitter = Button(frame_2, text="Quitter", command=fenetre.destroy)
bouton_quitter.pack(anchor=SE, padx=15, pady=15)

frame_3 = Frame(fenetre, width=WIDTH_PRAME_FIRST_LEVEL, height=210, bg=COLOR_2)
frame_3.pack(pady=5)
frame_3.propagate(False)

# ---------- Frame pour le resultat ---------- #
frame_3_1 = Frame(frame_3, width=300, height=220, bg=COLOR_3)
frame_3_1.pack(side=TOP, padx=5, pady=5)
frame_3_1.propagate(False)

text_result = Text(frame_3_1, width=280, height=200, bg=COLOR_4)
text_result.pack(side=TOP, padx=10, pady=10)

# calcul_determinant_matrice_de_2()

fenetre.mainloop()
