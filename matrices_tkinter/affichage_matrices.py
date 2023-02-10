# ********************* #
#  SVIATTSEVA Natalia   #
# ********************* #

from tkinter import *
from calcul_matrices import *


COLOR_1 = "#6096B4"
COLOR_2 = "#93BFCF"
COLOR_3 = "#BDCDD6"
COLOR_4 = "#EEE9DA"

SIZE = "500x600"
WIDTH_FRAME_1_LEVEL = 490


def get_matrice(mat):
    matrice = []
    idx = 0

    for i in mat.get("1.0", END).splitlines():
        if i != '':
            matrice.append([])
            for j in i.split(","):
                if j.lstrip("-").isnumeric():
                    matrice[idx].append((int(j)))
            idx += 1
    return matrice


def clear():
    text_result.delete('1.0', END)


def resultat_addition():
    mat_1 = get_matrice(input_matrice_1)
    mat_2 = get_matrice(input_matrice_2)
    matrice = addition(mat_1, mat_2)
    text_result.insert(END, f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")


def resultat_multiplication_par_scalaire():
    mat = get_matrice(input_matrice_1)
    matrice = multiplication_par_scalaire(mat, int(scalaire.get()))
    text_result.insert(END, f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")


def resultat_transition_matrice():
    mat = get_matrice(input_matrice_1)
    matrice = transition_matrice(mat)
    text_result.insert(END, f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")


def resultat_multiplication_matrices():
    mat_1 = get_matrice(input_matrice_1)
    mat_2 = get_matrice(input_matrice_2)
    matrice = multiplication_matrices(mat_1, mat_2)
    text_result.insert(END, f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")


def resultat_inversion_matrice_carre():
    mat_1 = get_matrice(input_matrice_1)
    matrice = calcul_inversion_matrice_carre(mat_1)
    text_result.insert(END, f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")


# Création de la fenêtre principale (main window)
fenetre = Tk()
fenetre.title("Calcul de matrices carré")
fenetre.geometry(SIZE)
fenetre.config(bg=COLOR_1)

# ---------- Première frame (Input frame) ---------- #
frame_1 = Frame(fenetre, width=WIDTH_FRAME_1_LEVEL, height=180, bg=COLOR_2)
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
frame_2 = Frame(fenetre, width=WIDTH_FRAME_1_LEVEL, height=180, bg=COLOR_2)
frame_2.pack(pady=5)
frame_2.propagate(False)

# ---------- Frame pour les boutons founctionels ---------- #
frame_2_1 = Frame(frame_2, width=220, height=170, bg=COLOR_3)
frame_2_1.pack(side=LEFT, padx=5, pady=5)
frame_2_1.propagate(False)

scalaire = Entry(frame_2)
scalaire.pack(anchor=NW, padx=15, pady=15)

bouton_addition_matrices = Button(frame_2_1, text="Addition Matrices", command=resultat_addition)
bouton_addition_matrices.pack(anchor=NW, padx=10, pady=4, fill=BOTH)

#
bouton_multiplication_scalaire = Button(frame_2_1, text="Multiplication Scalaire", command=resultat_multiplication_par_scalaire)
bouton_multiplication_scalaire.pack(padx=10, pady=4, fill=BOTH)
#
bouton_transition = Button(frame_2_1, text="Transition", command=resultat_transition_matrice)
bouton_transition.pack(padx=10, pady=4, fill=BOTH)

bouton_multiplication_matrices = Button(frame_2_1, text="Multiplication Matrices", command=resultat_multiplication_matrices)
bouton_multiplication_matrices.pack(padx=10, pady=4, fill=BOTH)

bouton_elimination = Button(frame_2_1, text="Elimination", command=resultat_inversion_matrice_carre)
bouton_elimination.pack(padx=10, pady=4, fill=BOTH)

bouton_quitter = Button(frame_2, text="Quitter", command=fenetre.destroy)
bouton_quitter.pack(anchor=NE, padx=15, pady=15)

frame_3 = Frame(fenetre, width=WIDTH_FRAME_1_LEVEL, height=210, bg=COLOR_2)
frame_3.pack(pady=5)
frame_3.propagate(False)

# ---------- Frame pour le resultat ---------- #
frame_3_1 = Frame(frame_3, width=300, height=220, bg=COLOR_3)
frame_3_1.pack(side=LEFT, padx=5, pady=5)
frame_3_1.propagate(False)

text_result = Text(frame_3_1, width=280, height=200, bg=COLOR_4)
text_result.pack(side=LEFT, padx=10, pady=10)

button_clear = Button(frame_3, text="Clear", command=clear)
button_clear.pack(anchor=NE, padx=15, pady=15)

fenetre.mainloop()
