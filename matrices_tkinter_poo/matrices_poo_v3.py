from tkinter import *
from calcul_matrices import *

COULEUR1 = "#ffff80"
COULEUR2 = "#9490ff"
COULEUR3 = "#fffe0b"
COULEUR4 = "#efecff"

SIZE = "460x580"


class Matrice(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master, bg=COULEUR1)
        self.grid()

        self.cadre1 = Frame(self.master, width=440, height=180, bg=COULEUR2, borderwidth=4, relief=GROOVE)
        self.cadre1.grid_propagate(False)
        self.cadre1.grid(padx=10, pady=10, stick='we')

        self.cadre2 = Frame(self.master, width=440, height=160, bg=COULEUR2, borderwidth=4, relief=GROOVE)
        self.cadre2.grid_propagate(False)
        self.cadre2.grid(padx=10, pady=10, stick='we')
        self.cadre2.grid_columnconfigure(0, weight=60)
        self.cadre2.grid_columnconfigure(1, weight=60)
        self.cadre2.grid_columnconfigure(2, weight=60)

        self.cadre3 = Frame(self.master, width=440, height=180, bg=COULEUR2, borderwidth=4, relief=GROOVE)
        self.cadre3.grid_propagate(False)
        self.cadre3.grid(padx=10, pady=10, stick='we')

        # self.matrice_1 = StringVar()
        # self.matrice_2 = StringVar()

        self.cadre()

    def cadre(self):
        Label(self.cadre1, text="Matrice 1 :", bg=COULEUR2).grid(row=0, column=0, padx=10, sticky=W)
        Label(self.cadre1, text="Matrice 2 :", bg=COULEUR2).grid(row=0, column=1, padx=10, sticky=W)
        Label(self.cadre1, text="Scalaire :", bg=COULEUR2).grid(row=0, column=2, padx=10, sticky=W)

        self.text_1 = Text(self.cadre1, width=18, height=8, bg=COULEUR4)
        self.text_1.grid(padx=10, row=1, column=0, sticky=N)
        self.text_2 = Text(self.cadre1, width=18, height=8, bg=COULEUR4)
        self.text_2.grid(padx=10, row=1, column=1, sticky=N)
        self.scalaire = Entry(self.cadre1, width=10, bg=COULEUR4)
        self.scalaire.grid(padx=10, row=1, column=2, sticky=N)

        Button(self.cadre2, text="Mult. Scalaire Mat. 1", background=COULEUR3, command=self.resultat_multiplication_par_scalaire_mat_1).grid(column=0, row=0, padx=5, pady=5, stick='we')
        Button(self.cadre2, text="Mult. Scalaire Mat. 2", background=COULEUR3, command=self.resultat_multiplication_par_scalaire_mat_2).grid(column=1, row=0, padx=5, pady=5, stick='we')
        Button(self.cadre2, text="Transition Mat. 1", background=COULEUR3, command=self.resultat_transition_matrice_1).grid(column=0, row=1, padx=5, pady=5, stick='we')
        Button(self.cadre2, text="Transition Mat. 2", background=COULEUR3, command=self.resultat_transition_matrice_2).grid(column=1, row=1, padx=5, pady=5, stick='we')
        Button(self.cadre2, text="Determ. Mat. 1", background=COULEUR3, command=self.resultat_determinant_matrice_1).grid(column=0, row=2, padx=5, pady=5, stick='we')
        Button(self.cadre2, text="Determ. Mat. 2", background=COULEUR3, command=self.resultat_determinant_matrice_2).grid(column=1, row=2, padx=5, pady=5, stick='we')
        Button(self.cadre2, text="Inversion Mat. 1", background=COULEUR3, command=self.resultat_inversion_matrice_1).grid(column=0, row=3, padx=5, pady=5, stick='we')
        Button(self.cadre2, text="Inversion Mat. 2", background=COULEUR3, command=self.resultat_inversion_matrice_2).grid(column=1, row=3, padx=5, pady=5, stick='we')
        Button(self.cadre2, text="Addition Matrices", background=COULEUR3, command=self.resultat_addition).grid(column=2, row=0, padx=5, pady=5, stick='we')
        Button(self.cadre2, text="Mult. Matrices", background=COULEUR3, command=self.resultat_multiplication_matrices).grid(column=2, row=1, padx=5, pady=5, stick='we')
        Button(self.cadre2, text="Quitter", background="red", command=fenetre.destroy).grid(column=2, row=3, padx=5, pady=5, stick='we')

        Label(self.cadre3, text="Resultat 1 :", bg=COULEUR2).grid(column=0, row=0, padx=10, sticky=W)
        self.text_result = Text(self.cadre3, width=50, height=8, bg=COULEUR4)
        self.text_result.grid(column=0, row=1, padx=10, stick='we')

    def get_matrice_1(self):
        self.matrice_1 = self.text_1.get("0.0", END)
        matrice = []
        idx = 0
        for i in self.matrice_1.splitlines():
            if i != '':
                matrice.append([])
                for j in i.split(","):
                    if j.lstrip("-").isnumeric():
                        matrice[idx].append((int(j)))
                idx += 1
        return matrice

    def get_matrice_2(self):
        self.matrice_2 = self.text_2.get("0.0", END)
        matrice = []
        idx = 0
        for i in self.matrice_2.splitlines():
            if i != '':
                matrice.append([])
                for j in i.split(","):
                    if j.lstrip("-").isnumeric():
                        matrice[idx].append((int(j)))
                idx += 1
        return matrice

    def resultat_multiplication_par_scalaire_mat_1(self):
        mat = self.get_matrice_1()
        matrice = multiplication_par_scalaire(mat, int(self.scalaire.get()))
        self.text_result.delete('1.0', END)
        self.text_result.insert(END, f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")

    def resultat_multiplication_par_scalaire_mat_2(self):
        mat = self.get_matrice_2()
        matrice = multiplication_par_scalaire(mat, int(self.scalaire.get()))
        self.text_result.delete('1.0', END)
        self.text_result.insert(END,f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")

    def resultat_transition_matrice_1(self):
        mat = self.get_matrice_1()
        matrice = transition_matrice(mat)
        self.text_result.delete('1.0', END)
        self.text_result.insert(END, (f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}"))

    def resultat_transition_matrice_2(self):
        mat = self.get_matrice_2()
        matrice = transition_matrice(mat)
        self.text_result.delete('1.0', END)
        self.text_result.insert(END, (f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}"))

    def resultat_determinant_matrice_1(self):
        mat = self.get_matrice_1()
        det = calcul_determinant_matrice_carre(mat)
        self.text_result.delete('1.0', END)
        self.text_result.insert(END, (f"{det}"))

    def resultat_determinant_matrice_2(self):
        mat = self.get_matrice_2()
        det = calcul_determinant_matrice_carre(mat)
        self.text_result.delete('1.0', END)
        self.text_result.insert(END, (f"{det}"))

    def resultat_inversion_matrice_1(self):
        mat_1 = self.get_matrice_1()
        matrice = calcul_inversion_matrice_carre(mat_1)
        self.text_result.delete('1.0', END)
        self.text_result.insert(END, f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")

    def resultat_inversion_matrice_2(self):
        mat_1 = self.get_matrice_2()
        matrice = calcul_inversion_matrice_carre(mat_1)
        self.text_result.delete('1.0', END)
        self.text_result.insert(END, f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")

    def resultat_addition(self):
        mat_1 = self.get_matrice_1()
        mat_2 = self.get_matrice_2()
        matrice = addition(mat_1, mat_2)
        self.text_result.delete('1.0', END)
        self.text_result.insert(END, f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")

    def resultat_multiplication_matrices(self):
        mat_1 = self.get_matrice_1()
        mat_2 = self.get_matrice_2()
        matrice = multiplication_matrices(mat_1, mat_2)
        self.text_result.delete('1.0', END)
        self.text_result.insert(END, f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")


if __name__ == "__main__":
    fenetre = Tk()
    fenetre.title("НЕЧТО")
    fenetre.geometry(SIZE)
    fenetre["bg"] = COULEUR1
    Matrice(fenetre)
    fenetre.mainloop()



