# https://trello.com/b/uocjRWxK/tableau-agile

from tkinter import *

from PIL.Image import Resampling

from constantes import *
from personnage import *
from artefacts import Artefacts
from PIL import Image, ImageTk

TAILLE = "1200x600"


class Main(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.personnage = liste_personnages[0][1]
        self.personnage_choisit = liste_personnages[0][0]
        self.personnage_image = liste_personnages[0][2]
        self.choice_personnage = StringVar()

        self.ennemi = liste_ennemis[0][1]
        self.ennemi_choisit = liste_ennemis[0][0]
        self.ennemi_image = liste_ennemis[0][2]
        self.choice_ennemi = StringVar()

        self.race_label = StringVar()
        self.nom_label = StringVar()
        self.sante_label = StringVar()
        self.force_label = StringVar()
        self.endurance_label = StringVar()
        self.agilite_label = StringVar()
        self.defense_label = StringVar()
        self.intelligence_label = StringVar()

        self.master = master
        self.barre_de_menu()
        self.nom_du_jeu()
        self.personnage_affichage()
        self.sauron_affichage()
        self.journal()

    def barre_de_menu(self):
        """ Affichage de menu """
        # TODO-1: menu avec options : choisir le personnage, regles du jeu et sortie
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.master.destroy)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menu.add_command(label="Choisir le personnage", command=self.fenetre_choisir_personnage)

    def fenetre_choisir_personnage(self):
        self.fenetre_nouveau = Toplevel(root)
        self.fenetre_nouveau.title("Choisir le personnage")
        self.fenetre_nouveau.geometry("240x280")
        self.radiobuttons_personnages()
        self.bouton_choisir_personnage()
        # self.radiobuttons_ennemis()
        # self.bouton_choisir_ennemi()

    def radiobuttons_personnages(self):
        self.cadre_radioboutons_personnage = Frame(self.fenetre_nouveau, borderwidth=4, relief=GROOVE)
        self.cadre_radioboutons_personnage.grid(row=0, column=0, padx=5, pady=5)
        for i in range(len(liste_personnages)):
            self.radiobutton_personnages = Radiobutton(self.cadre_radioboutons_personnage, text=liste_personnages[i][0],
                                                       variable=self.choice_personnage, value=liste_personnages[i][0],
                                                       anchor="nw")
            self.radiobutton_personnages.grid_propagate(False)
            self.radiobutton_personnages.grid(row=i, column=0, padx=5, pady=5)

    def radiobuttons_ennemis(self):
        self.cadre_radioboutons_enemies = Frame(self.fenetre_nouveau, borderwidth=4, relief=GROOVE)
        self.cadre_radioboutons_enemies.grid(row=0, column=1, padx=5, pady=5)
        for i in range(len(liste_ennemis)):
            self.radiobutton_enemies = Radiobutton(self.cadre_radioboutons_enemies, text=liste_ennemis[i][0],
                                                   variable=self.choice_ennemi, value=liste_ennemis[i][0])
            self.radiobutton_enemies.grid_propagate(False)
            self.radiobutton_enemies.grid(row=i, column=1, padx=5, pady=5)

    def bouton_choisir_personnage(self):
        bouton_choisir_personnage = Button(self.cadre_radioboutons_personnage, text="Choisir Pers",
                                           command=self.definir_personnage)
        bouton_choisir_personnage.grid_propagate(False)
        bouton_choisir_personnage.grid(row=200, column=0, padx=5, pady=5)

    def bouton_choisir_ennemi(self):
        bouton_choisir_enemie = Button(self.cadre_radioboutons_enemies, text="Choisir Enem",
                                       command=self.definir_ennemi)
        bouton_choisir_enemie.grid_propagate(False)
        bouton_choisir_enemie.grid(row=200, column=1, padx=5, pady=5)

    def definir_personnage(self):
        self.personnage_choisit = self.choice_personnage.get()
        for i in range(len(liste_personnages)):
            if self.personnage_choisit == liste_personnages[i][0]:
                self.personnage = liste_personnages[i][1]
                self.personnage_image = liste_personnages[i][2]
        self.add_photo(self.cadre_personnage, 160, 220, self.personnage_image)
        self.caracteristiques(self.cadre_caract_personnage, self.personnage)

    def definir_ennemi(self):
        self.enemie_choisit = self.choice_ennemi.get()
        for i in range(len(liste_ennemis)):
            if self.enemie_choisit == liste_ennemis[i][0]:
                self.enemie = liste_ennemis[i][1]
                self.enemie_image = liste_ennemis[i][2]
        self.add_photo(self.cadre_sauron, 160, 220, self.enemie_image)
        self.caracteristiques(self.cadre_caract_sauron, self.enemie)

    def nom_du_jeu(self):
        """ Affichage de nom du jeu """
        self.cadre_nom_du_jeu = Frame(self.master, width=1180, height=115, borderwidth=4, relief=GROOVE)
        self.cadre_nom_du_jeu.propagate(False)
        self.cadre_nom_du_jeu.pack(padx=10, pady=10, anchor='n')
        # appele de founction pour afficher l'image
        self.add_photo(self.cadre_nom_du_jeu, 1140, 100, f"images\\logo.png")

    def personnage_affichage(self):
        # Cadre pour elements de Frodon :
        # image
        # caractéristiques
        # artefacts
        self.cadre1 = Frame(self.master, width=380, height=420, borderwidth=4, relief=GROOVE)
        self.cadre1.propagate(False)
        self.cadre1.pack(padx=10, pady=10, side=LEFT)
        # Cadre pour l'image du Frodon
        self.cadre_personnage = Frame(self.cadre1, width=180, height=240, borderwidth=4, relief=GROOVE)
        self.cadre_personnage.grid_propagate(False)
        self.cadre_personnage.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.add_photo(self.cadre_personnage, 160, 220, self.personnage_image)
        # Cadre pour caractéristiques du Frodon
        self.cadre_caract_personnage = Frame(self.cadre1, width=160, height=240, borderwidth=4, relief=GROOVE)
        self.cadre_caract_personnage.grid_propagate(False)
        self.cadre_caract_personnage.grid(row=0, column=1, padx=5, pady=5, sticky=NE)
        self.caracteristiques(self.cadre_caract_personnage, self.personnage)
        # cadre pour boutons du actions de Frodon
        self.cadre_boutons_personnage = Frame(self.cadre1, width=350, height=140, borderwidth=4, relief=GROOVE)
        self.cadre_boutons_personnage.grid_propagate(False)
        self.cadre_boutons_personnage.grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky=W)
        # Bouton pour attaque Frodon
        self.bouton_attaque_personnage = Button(self.cadre_boutons_personnage, text="Attaque",
                                                command=self.attaque_de_personnage)
        self.bouton_attaque_personnage.grid(row=0, column=0, padx=10, sticky=W)
        self.bouton_perdre_sante_personnage = Button(self.cadre_boutons_personnage, text="Sante -5",
                                                     command=self.perdre_sante_personnage)
        self.bouton_perdre_sante_personnage.grid(row=0, column=1, padx=10, sticky=W)
        self.bouton_soigne_sante_personnage = Button(self.cadre_boutons_personnage, text="Sante +5",
                                                     command=self.soigne_sante_personnage)
        self.bouton_soigne_sante_personnage.grid(row=0, column=2, padx=10, sticky=W)
        # Epee: + force, armure: + defence, bottes: + agilite
        self.var = IntVar()
        self.epee_personnage = Checkbutton(self.cadre_boutons_personnage, text="Epee", variable=self.var, onvalue=1,
                                           offvalue=0,
                                           command=self.epee)
        self.epee_personnage.grid(row=1, column=0, padx=10, sticky=W)
        # self.armure_personage = Checkbutton(self.cadre_boutons_personnage, text="Armure", variable=self.var, onvalue=1,
        #                                    offvalue=0,
        #                                    command=self.armure)
        # self.armure_personage.grid(row=1, column=1, padx=10, sticky=W)
        # self.bottes_personnage = Checkbutton(self.cadre_boutons_personnage, text="Bottes", variable=self.var, onvalue=1,
        #                                    offvalue=0,
        #                                    command=self.bottes)
        # self.bottes_personnage.grid(row=1, column=2, padx=10, sticky=W)

        self.bouton_autobataille = Button(self.cadre_boutons_personnage, text="Autobataille",
                                          command=self.autobataille)
        self.bouton_autobataille.grid_propagate()
        self.bouton_autobataille.grid(row=100, column=100)

    def sauron_affichage(self):
        #
        # Cadre pour elements de Sauron :
        # image
        # caractéristiques
        # artefacts
        self.cadre2 = Frame(self.master, width=380, height=420, borderwidth=4, relief=GROOVE)
        self.cadre2.propagate(False)
        self.cadre2.pack(padx=10, pady=10, side=LEFT)
        # Cadre pour l'image du Sauron
        self.cadre_sauron = Frame(self.cadre2, width=180, height=240, borderwidth=4, relief=GROOVE)
        self.cadre_sauron.grid_propagate(False)
        self.cadre_sauron.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.add_photo(self.cadre_sauron, 160, 220, f"images\\sauron.png")
        # Cadre pour caractéristiques du Sauron
        self.cadre_caract_sauron = Frame(self.cadre2, width=160, height=240, borderwidth=4, relief=GROOVE)
        self.cadre_caract_sauron.grid_propagate(False)
        self.cadre_caract_sauron.grid(row=0, column=1, padx=5, pady=5, sticky=NE)
        self.caracteristiques(self.cadre_caract_sauron, sauron)
        # cadre pour boutons du actions de Sauron
        self.cadre_boutons_sauron = Frame(self.cadre2, width=350, height=140, borderwidth=4, relief=GROOVE)
        self.cadre_boutons_sauron.grid_propagate(False)
        self.cadre_boutons_sauron.grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky=W)
        # Bouton pour attaque Sauron
        self.bouton_attaque_sauron = Button(self.cadre_boutons_sauron, text="Attaque",
                                            command=self.attaque_de_sauron)
        self.bouton_attaque_sauron.grid(row=0, column=0, padx=10, sticky=W)
        #
        self.bouton_perdre_sante_sauron = Button(self.cadre_boutons_sauron, text="Sante -5",
                                                 command=self.perdre_sante_sauron)
        self.bouton_perdre_sante_sauron.grid(row=0, column=1, padx=10, sticky=W)
        self.bouton_soigne_sante_sauron = Button(self.cadre_boutons_sauron, text="Sante +5",
                                                 command=self.soigne_sante_sauron)
        self.bouton_soigne_sante_sauron.grid(row=0, column=2, padx=10, sticky=W)

    def journal(self):
        self.cadre3 = Frame(self.master, width=380, height=480, borderwidth=4, relief=GROOVE)
        self.cadre3.propagate(False)
        self.cadre3.pack(padx=10, pady=10, side=LEFT)
        self.log = Text(self.cadre3, width=340, height=440)
        self.log.pack(padx=10, pady=10, side=LEFT)

    def add_photo(self, cadre, w, h, file_name):
        image = Image.open(file_name).resize((w, h), Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        label1 = Label(cadre, image=photo)
        label1.image = photo
        label1.place(x=0, y=0)

    def caracteristiques(self, cadre, qui):
        self.set_caracteristiques(qui)
        self.affiche_caracteristiques(cadre)

    def set_caracteristiques(self, qui):
        self.race_label.set(f"Race : {qui.race}")
        self.nom_label.set(f"Nom : {qui.nom}")
        # if qui.sante <= 0:
        #     self.label_sante = self.sante_label.set(f"Sante : MORT")
        # else:
        self.label_sante = self.sante_label.set(f"Sante : {qui.sante}")
        self.force_label.set(f"Force : {qui.force}")
        self.endurance_label.set(f"Endurance : {qui.endurance}")
        self.agilite_label.set(f"Agilite : {qui.agilite}")
        self.defense_label.set(f"Defense : {qui.defense}")
        self.intelligence_label.set(f"Intelligence : {qui.intelligence}")

    def affiche_caracteristiques(self, cadre):
        # caractéristiques du personnage
        Label(cadre, textvariable=self.race_label).grid(row=0, column=0, padx=5, sticky=W)
        Label(cadre, textvariable=self.nom_label).grid(row=1, column=0, padx=5, sticky=W)
        Label(cadre, textvariable=self.sante_label).grid(row=2, column=0, padx=5, sticky=W)
        Label(cadre, textvariable=self.force_label).grid(row=3, column=0, padx=5, sticky=W)
        Label(cadre, textvariable=self.endurance_label).grid(row=4, column=0, padx=5, sticky=W)
        Label(cadre, textvariable=self.agilite_label).grid(row=5, column=0, padx=5, sticky=W)
        Label(cadre, textvariable=self.defense_label).grid(row=6, column=0, padx=5, sticky=W)
        Label(cadre, textvariable=self.intelligence_label).grid(row=7, column=0, padx=5, sticky=W)
        # Label(cadre, text=f"Magie : {personnage.magie}").grid(row=8, column=0, padx=5, sticky=W)
        # Label(cadre, text=f"Karma : {personnage.karma}").grid(row=9, column=0, padx=5, sticky=W)

    def attaque_de_personnage(self):
        attaque = self.personnage.attaque(sauron)
        self.caracteristiques(self.cadre_caract_personnage, self.personnage)
        self.caracteristiques(self.cadre_caract_sauron, sauron)
        self.log.insert(END, f"{attaque}\n")

    def attaque_de_sauron(self):
        attaque = sauron.attaque(self.personnage)
        self.caracteristiques(self.cadre_caract_personnage, self.personnage)
        self.caracteristiques(self.cadre_caract_sauron, sauron)
        self.log.insert(END, f"{attaque}\n")

    def perdre_sante_personnage(self):
        action = self.personnage.perdre_sante(5)
        self.caracteristiques(self.cadre_caract_personnage, self.personnage)
        self.log.insert(END, f"{action}\n")

    def soigne_sante_personnage(self):
        action = self.personnage.gagne_sante(5)
        self.caracteristiques(self.cadre_caract_personnage, self.personnage)
        self.log.insert(END, f"{action}\n")

    def perdre_sante_sauron(self):
        action = sauron.perdre_sante(5)
        self.caracteristiques(self.cadre_caract_sauron, sauron)
        self.log.insert(END, f"{action}\n")

    def soigne_sante_sauron(self):
        action = sauron.gagne_sante(5)
        self.caracteristiques(self.cadre_caract_sauron, sauron)
        self.log.insert(END, f"{action}\n")

    def armure(self):
        if self.var.get() == 1:
            action = Artefacts.utiliser_armure(self.personnage)
            self.set_caracteristiques(self.personnage)
            self.log.insert(END, f"{action}\n")
        else:
            action = Artefacts.jeter_epee(self.personnage)
            self.set_caracteristiques(self.personnage)
            self.log.insert(END, f"{action}\n")

    def epee(self):
        if self.var.get() == 1:
            action = Artefacts.utiliser_epee(self.personnage)
            self.set_caracteristiques(self.personnage)
            self.log.insert(END, f"{action}\n")
        else:
            action = Artefacts.jeter_epee(self.personnage)
            self.set_caracteristiques(self.personnage)
            self.log.insert(END, f"{action}\n")

    def bottes(self):
        if self.var.get() == 1:
            action = Artefacts.utiliser_bottes(self.personnage)
            self.set_caracteristiques(self.personnage)
            self.log.insert(END, f"{action}\n")
        else:
            action = Artefacts.jeter_epee(self.personnage)
            self.set_caracteristiques(self.personnage)
            self.log.insert(END, f"{action}\n")


    def autobataille(self):
        bataille = self.personnage.autobataille(sauron)
        self.caracteristiques(self.cadre_caract_personnage, self.personnage)
        self.caracteristiques(self.cadre_caract_sauron, sauron)
        self.log.insert(END, f"{bataille}\n")


root = Tk()
app = Main(root)
root.geometry(TAILLE)

root.mainloop()
