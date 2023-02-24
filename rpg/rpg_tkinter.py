# https://trello.com/b/uocjRWxK/tableau-agile

from tkinter import *
from constantes import *
from personnage import *
from artefacts import *
from PIL import Image, ImageTk


TAILLE = "1200x500"


class Main(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # TODO-1: menu avec options : choisir le personnage, regles du jeu et sortie
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.master.destroy)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)

        # Cadre pour nom du jeu
        self.cadre_nom_du_jeu = Frame(self.master, width=1180, height=40, borderwidth=4, relief=GROOVE)
        self.cadre_nom_du_jeu.propagate(False)
        self.cadre_nom_du_jeu.pack(padx=10, pady=10, anchor='n')

        # Cadre pour elements de Personnage 1 :
        # image
        # caractéristiques
        # artefacts
        self.cadre1 = Frame(self.master, width=380, height=420, borderwidth=4, relief=GROOVE)
        self.cadre1.propagate(False)
        self.cadre1.pack(padx=10, pady=10, side=LEFT)

        # Cadre pour l'image du Personnage 1
        self.cadre_pers_1 = Frame(self.cadre1, width=180, height=240, borderwidth=4, relief=GROOVE)
        self.cadre_pers_1.grid_propagate(False)
        self.cadre_pers_1.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.add_photo(self.cadre_pers_1, f"images\\frodon.png")  # appele de founction pour afficher l'image

        # Cadre pour caractéristiques du Personnage 1
        self.cadre_caract_pers_1 = Frame(self.cadre1, width=160, height=240, borderwidth=4, relief=GROOVE)
        self.cadre_caract_pers_1.grid_propagate(False)
        self.cadre_caract_pers_1.grid(row=0, column=1, padx=5, pady=5, sticky=NE)

        self.affiche_caracteristiques(self.cadre_caract_pers_1, frodon_sacquet)

        # cadre pour boutons du actions de Personnage 1
        self.cadre_boutons_pers_1 = Frame(self.cadre1, width=350, height=140, borderwidth=4, relief=GROOVE)
        self.cadre_boutons_pers_1.grid_propagate(False)
        self.cadre_boutons_pers_1.grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky=W)

        # Bouton pour attaque Personnage 1
        self.bouton_attaque_pers_1 = Button(self.cadre_boutons_pers_1, text="Attaque", command=self.attaque_pers_1)
        self.bouton_attaque_pers_1.grid(row=0, column=0, padx=10, sticky=W)

        self.bouton_perdre_sante_pers_1 = Button(self.cadre_boutons_pers_1, text="Sante -1", command=self.perdre_sante_pers_1)
        self.bouton_perdre_sante_pers_1.grid(row=0, column=2, padx=10, sticky=W)

        # CheckBox, mais pour tester mainenant c'est le bouton
        # self.bouton_epee = Button(self.cadre_boutons_pers_1, text="Eppe", command=self.epee)
        # self.bouton_epee.grid(row=0, column=1, padx=10, sticky=W)

        # Cadre pour elements de Personnage 2 :
        # image
        # caractéristiques
        # artefacts
        self.cadre2 = Frame(self.master, width=380, height=420, borderwidth=4, relief=GROOVE)
        self.cadre2.propagate(False)
        self.cadre2.pack(padx=10, pady=10, side=LEFT)

        # Cadre pour l'image du Personnage 2
        self.cadre_pers_2 = Frame(self.cadre2, width=180, height=240, borderwidth=4, relief=GROOVE)
        self.cadre_pers_2.grid_propagate(False)
        self.cadre_pers_2.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.add_photo(self.cadre_pers_2, f"images\\sauron.png")  # appele de founction pour afficher l'image

        # Cadre pour caractéristiques du Personnage 2
        self.cadre_caract_pers_2 = Frame(self.cadre2, width=160, height=240, borderwidth=4, relief=GROOVE)
        self.cadre_caract_pers_2.grid_propagate(False)
        self.cadre_caract_pers_2.grid(row=0, column=1, padx=5, pady=5, sticky=NE)

        self.affiche_caracteristiques(self.cadre_caract_pers_2, sauron)

        # cadre pour boutons du actions de Personnage 2
        self.cadre_boutons_pers_2 = Frame(self.cadre2, width=350, height=140, borderwidth=4, relief=GROOVE)
        self.cadre_boutons_pers_2.grid_propagate(False)
        self.cadre_boutons_pers_2.grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky=W)

        # Bouton pour attaque Personnage 2
        self.bouton_attaque_pers_2 = Button(self.cadre_boutons_pers_2, text="Attaque", command=self.attaque_pers_1)
        self.bouton_attaque_pers_2.grid(row=10, column=0, padx=10, sticky=W)

        self.cadre3 = Frame(self.master, width=380, height=480, borderwidth=4, relief=GROOVE)
        self.cadre3.propagate(False)
        self.cadre3.pack(padx=10, pady=10, side=LEFT)

        self.log = Text(self.cadre3, width=340, height=440)
        self.log.pack(padx=10, pady=10, side=LEFT)

    def add_photo(self, cadre, file_name):
        global photo
        image = Image.open(file_name)
        photo = ImageTk.PhotoImage(image)
        canvas = Canvas(cadre, width=175, height=235)
        canvas.create_image(0, 0, anchor=NW, image=photo)
        canvas.pack()

    def affiche_caracteristiques(self, cadre, personnage):
        # caractéristiques du personnage
        Label(cadre, text=f"Race : {personnage.race}").grid(row=0, column=0, padx=5, sticky=W)
        Label(cadre, text=f"Nom : {personnage.nom}").grid(row=1, column=0, padx=5, sticky=W)
        self.label_sante = Label(cadre, text=f"Sante : {personnage.sante}")
        self.label_sante.grid(row=2, column=0, padx=5, sticky=W)
        Label(cadre, text=f"Force : {personnage.force}").grid(row=3, column=0, padx=5, sticky=W)
        Label(cadre, text=f"Endurance : {personnage.endurance}").grid(row=4, column=0, padx=5, sticky=W)
        Label(cadre, text=f"Agilite : {personnage.agilite}").grid(row=5, column=0, padx=5, sticky=W)
        Label(cadre, text=f"Defense : {personnage.defense}").grid(row=6, column=0, padx=5, sticky=W)
        Label(cadre, text=f"Intelligence : {personnage.intelligence}").grid(row=7, column=0, padx=5, sticky=W)
        Label(cadre, text=f"Magie : {personnage.magie}").grid(row=8, column=0, padx=5, sticky=W)
        Label(cadre, text=f"Karma : {personnage.karma}").grid(row=9, column=0, padx=5, sticky=W)

        # global photo_image
        # photo_image = PhotoImage(file="images\\frodo.png")
        # self.label_image = Label(self.cadre_pers_1, image=photo_image)
        # self.label_image.pack(side=TOP, padx=10, pady=10)

    def attaque_pers_1(self):
        attaque = frodon_sacquet.attaque(sauron)
        self.log.insert(END, f"{attaque}\n")

    def perdre_sante_pers_1(self):
        action = frodon_sacquet.perdre_sante(5)
        self.affiche_caracteristiques(self.cadre_caract_pers_1, frodon_sacquet)
        self.log.insert(END, f"{action}\n")
        if frodon_sacquet.est_mort():
            self.bouton_perdre_sante_pers_1["state"] = DISABLED
            self.label_sante.config(text="MORT", fg="red")

    # def epee(self):
    #     frodon_sacquet.apliquier_epee()
    #     self.apliquier_epee(frodon_sacquet)
    #     self.affiche_caracteristiques(self.cadre_caract_pers_1, frodon_sacquet)

root = Tk()
app = Main(root)
root.geometry(TAILLE)

root.mainloop()
