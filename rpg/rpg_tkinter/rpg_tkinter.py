from tkinter import *

from PIL.Image import Resampling

from constantes import *
from artefacts import Artefacts
from PIL import Image, ImageTk

TAILLE = "1200x600"


class Main(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.personnage_gentil = liste_personnages_gentils[0][0]
        self.image_du_personnage_gentil = liste_personnages_gentils[0][1]
        self.choix_personnage_gentil = StringVar()

        self.personnage_mechant = liste_personnages_mechants[0][0]
        self.image_du_personnage_mechant = liste_personnages_mechants[0][1]
        self.choix_personnage_mechant = StringVar()

        self.race_personnage_gentil = StringVar()
        self.nom_personnage_gentil = StringVar()
        self.sante_personnage_gentil = StringVar()
        self.force_personnage_gentil = StringVar()
        self.endurance_personnage_gentil = StringVar()
        self.agilite_personnage_gentil = StringVar()
        self.defense_personnage_gentil = StringVar()
        self.intelligence_personnage_gentil = StringVar()

        self.race_personnage_mechant = StringVar()
        self.nom_personnage_mechant = StringVar()
        self.sante_personnage_mechant = StringVar()
        self.force_personnage_mechant = StringVar()
        self.endurance_personnage_mechant = StringVar()
        self.agilite_personnage_mechant = StringVar()
        self.defense_personnage_mechant = StringVar()
        self.intelligence_personnage_mechant = StringVar()

        self.master = master
        self.master.grid_columnconfigure(0, minsize=115)
        self.master.grid_columnconfigure(1, minsize=115)
        self.master.grid_rowconfigure(0, minsize=115)
        self.master.grid_rowconfigure(1, minsize=115)
        self.master.grid_rowconfigure(2, minsize=115)

        self.barre_de_menu()
        self.nom_du_jeu()
        self.jeu_principal()

    def barre_de_menu(self):
        """ Affichage du menu """
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
        self.fenetre_nouveau.geometry("340x380")
        self.choisir_personnages()

    def choisir_personnages(self):
        self.choisir_personnage(liste_personnages_gentils, self.choix_personnage_gentil, number=0,
                                action=self.definir_personnage_gentil)
        self.choisir_personnage(liste_personnages_mechants, self.choix_personnage_mechant, number=1,
                                action=self.definir_personnage_mechant)

    def choisir_personnage(self, liste, choix_personnage, number, action):
        self.cadre_choisir_personnage = Frame(self.fenetre_nouveau, borderwidth=4, relief=GROOVE)
        self.cadre_choisir_personnage.grid(row=0, column=number, padx=5, pady=5)
        for i in range(len(liste)):
            self.radiobutton_personnages = Radiobutton(self.cadre_choisir_personnage,
                                                       text=liste[i][0].nom,
                                                       variable=choix_personnage,
                                                       value=liste[i][0].nom,
                                                       anchor="nw")
            self.radiobutton_personnages.grid_propagate(False)
            self.radiobutton_personnages.grid(row=i, column=0, padx=5, pady=5)

        bouton_choisir_personnage = Button(self.cadre_choisir_personnage, text="Choisir",
                                           command=action)
        bouton_choisir_personnage.grid_propagate(False)
        bouton_choisir_personnage.grid(row=200, column=0, padx=5, pady=5)

    def definir_personnage_gentil(self):
        self.nom_de_personnage_choisit = self.choix_personnage_gentil.get()
        for i in range(len(liste_personnages_gentils)):
            if self.nom_de_personnage_choisit == liste_personnages_gentils[i][0].nom:
                self.personnage_gentil = liste_personnages_gentils[i][0]
                self.image_du_personnage_gentil = liste_personnages_gentils[i][1]
        self.add_photo(self.cadre_image_personnage_gentil, 160, 220, self.image_du_personnage_gentil)
        self.set_caracteristiques_personnage_gentil()

    def definir_personnage_mechant(self):
        self.nom_de_personnage_choisit = self.choix_personnage_mechant.get()
        for i in range(len(liste_personnages_mechants)):
            if self.nom_de_personnage_choisit == liste_personnages_mechants[i][0].nom:
                self.personnage_mechant = liste_personnages_mechants[i][0]
                self.image_du_personnage_mechant = liste_personnages_mechants[i][1]
        self.add_photo(self.cadre_image_personnage_mechant, 160, 220, self.image_du_personnage_mechant)
        self.set_caracteristiques_personnage_mechant()

    def nom_du_jeu(self):
        """ Affichage de nom du jeu """
        self.cadre_nom_du_jeu = Frame(self.master, width=1180, height=115, borderwidth=4, relief=GROOVE)
        self.cadre_nom_du_jeu.grid_propagate(False)
        self.cadre_nom_du_jeu.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        # appele de founction pour afficher l'image
        self.add_photo(self.cadre_nom_du_jeu, 1140, 100, f"images\\logo.png")

    def jeu_principal(self):
        self.cadre_jeu_principal = Frame(self.master, width=1180, height=460, borderwidth=4, relief=GROOVE)
        self.cadre_jeu_principal.grid_propagate(False)
        self.cadre_jeu_principal.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        self.personnage_affichage_gentil()
        self.personnage_affichage_mechant()
        self.journal()

    def personnage_affichage_gentil(self):
        self.cadre_personnage_gentil = Frame(self.cadre_jeu_principal, width=380, height=440, borderwidth=4,
                                             relief=GROOVE)
        self.cadre_personnage_gentil.grid_propagate(False)
        self.cadre_personnage_gentil.grid(row=0, column=0, padx=5, pady=5)
        # Cadre pour l'image du Personnage
        self.cadre_image_personnage_gentil = Frame(self.cadre_personnage_gentil, width=180, height=240, borderwidth=4,
                                                   relief=GROOVE)
        self.cadre_image_personnage_gentil.grid_propagate(False)
        self.cadre_image_personnage_gentil.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.add_photo(self.cadre_image_personnage_gentil, 160, 220, self.image_du_personnage_gentil)

        # Cadre pour caractéristiques du Personnage
        self.cadre_caract_personnage_gentil = Frame(self.cadre_personnage_gentil, width=160, height=240, borderwidth=4,
                                                    relief=GROOVE)
        self.cadre_caract_personnage_gentil.grid_propagate(False)
        self.cadre_caract_personnage_gentil.grid(row=0, column=1, padx=5, pady=5, sticky=NE)

        # caractéristiques du personnage
        self.set_caracteristiques_personnage_gentil()
        Label(self.cadre_caract_personnage_gentil, textvariable=self.race_personnage_gentil).grid(row=0, column=0,
                                                                                                  padx=5, sticky=W)
        Label(self.cadre_caract_personnage_gentil, textvariable=self.nom_personnage_gentil).grid(row=1, column=0,
                                                                                                 padx=5, sticky=W)
        Label(self.cadre_caract_personnage_gentil, textvariable=self.sante_personnage_gentil).grid(row=2, column=0,
                                                                                                   padx=5, sticky=W)
        Label(self.cadre_caract_personnage_gentil, textvariable=self.force_personnage_gentil).grid(row=3, column=0,
                                                                                                   padx=5, sticky=W)
        Label(self.cadre_caract_personnage_gentil, textvariable=self.endurance_personnage_gentil).grid(row=4, column=0,
                                                                                                       padx=5, sticky=W)
        Label(self.cadre_caract_personnage_gentil, textvariable=self.agilite_personnage_gentil).grid(row=5, column=0,
                                                                                                     padx=5, sticky=W)
        Label(self.cadre_caract_personnage_gentil, textvariable=self.defense_personnage_gentil).grid(row=6, column=0,
                                                                                                     padx=5, sticky=W)
        Label(self.cadre_caract_personnage_gentil, textvariable=self.intelligence_personnage_gentil).grid(row=7,
                                                                                                          column=0,
                                                                                                          padx=5,
                                                                                                          sticky=W)

        # cadre pour boutons du actions du Personnage
        self.cadre_boutons_personnage_gentil = Frame(self.cadre_personnage_gentil, width=350, height=140, borderwidth=4,
                                                     relief=GROOVE)
        self.cadre_boutons_personnage_gentil.grid_propagate(False)
        self.cadre_boutons_personnage_gentil.grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky=W)

        # Bouton pour attaque du Personnage
        self.bouton_attaque_personnage_gentil = Button(self.cadre_boutons_personnage_gentil, text="Attaque",
                                                       command=self.attaque_de_personnage_gentil)
        self.bouton_attaque_personnage_gentil.grid(row=0, column=0, padx=5, sticky=W)
        self.bouton_perdre_sante_personnage_gentil = Button(self.cadre_boutons_personnage_gentil, text="Sante -5",
                                                            command=self.perdre_sante_personnage_gentil)
        self.bouton_perdre_sante_personnage_gentil.grid(row=0, column=1, padx=5, sticky=W)
        self.bouton_soigne_sante_personnage_gentil = Button(self.cadre_boutons_personnage_gentil, text="Sante +5",
                                                            command=self.soigne_sante_personnage_gentil)
        self.bouton_soigne_sante_personnage_gentil.grid(row=0, column=2, padx=5, sticky=W)
        # Epee: + force, armure: + defence, bottes: + agilite
        self.var_epee = IntVar()
        self.var_armure = IntVar()
        self.var_bottes = IntVar()

        self.epee_personnage_gentil = Checkbutton(self.cadre_boutons_personnage_gentil, text="Epee",
                                                  variable=self.var_epee,
                                                  onvalue=1,
                                                  offvalue=0,
                                                  command=self.epee)
        self.epee_personnage_gentil.grid(row=1, column=0, padx=5, sticky=W)
        self.armure_personage_gentil = Checkbutton(self.cadre_boutons_personnage_gentil, text="Armure",
                                                   variable=self.var_armure, onvalue=1,
                                                   offvalue=0,
                                                   command=self.armure)
        self.armure_personage_gentil.grid(row=1, column=1, padx=5, sticky=W)
        self.bottes_personnage_gentil = Checkbutton(self.cadre_boutons_personnage_gentil, text="Bottes",
                                                    variable=self.var_bottes, onvalue=1,
                                                    offvalue=0,
                                                    command=self.bottes)
        self.bottes_personnage_gentil.grid(row=1, column=2, padx=5, sticky=W)

        self.bouton_autobataille = Button(self.cadre_boutons_personnage_gentil, text="Autobataille",
                                          command=self.autobataille)
        self.bouton_autobataille.grid_propagate()
        self.bouton_autobataille.grid(row=100, column=100)

    def personnage_affichage_mechant(self):
        self.cadre_personnage_mechant = Frame(self.cadre_jeu_principal, width=380, height=440, borderwidth=4,
                                              relief=GROOVE)
        self.cadre_personnage_mechant.grid_propagate(False)
        self.cadre_personnage_mechant.grid(row=0, column=1, padx=5, pady=5)
        # Cadre pour l'image du Personnage
        self.cadre_image_personnage_mechant = Frame(self.cadre_personnage_mechant, width=180, height=240, borderwidth=4,
                                                    relief=GROOVE)
        self.cadre_image_personnage_mechant.grid_propagate(False)
        self.cadre_image_personnage_mechant.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.add_photo(self.cadre_image_personnage_mechant, 160, 220, self.image_du_personnage_mechant)

        # Cadre pour caractéristiques du Personnage
        self.cadre_caract_personnage_mechant = Frame(self.cadre_personnage_mechant, width=160, height=240,
                                                     borderwidth=4,
                                                     relief=GROOVE)
        self.cadre_caract_personnage_mechant.grid_propagate(False)
        self.cadre_caract_personnage_mechant.grid(row=0, column=1, padx=5, pady=5, sticky=NE)
        # caractéristiques du personnage
        self.set_caracteristiques_personnage_mechant()
        Label(self.cadre_caract_personnage_mechant, textvariable=self.race_personnage_mechant).grid(row=0, column=0,
                                                                                                    padx=5, sticky=W)
        Label(self.cadre_caract_personnage_mechant, textvariable=self.nom_personnage_mechant).grid(row=1, column=0,
                                                                                                   padx=5, sticky=W)
        Label(self.cadre_caract_personnage_mechant, textvariable=self.sante_personnage_mechant).grid(row=2, column=0,
                                                                                                     padx=5, sticky=W)
        Label(self.cadre_caract_personnage_mechant, textvariable=self.force_personnage_mechant).grid(row=3, column=0,
                                                                                                     padx=5, sticky=W)
        Label(self.cadre_caract_personnage_mechant, textvariable=self.endurance_personnage_mechant).grid(row=4,
                                                                                                         column=0,
                                                                                                         padx=5,
                                                                                                         sticky=W)
        Label(self.cadre_caract_personnage_mechant, textvariable=self.agilite_personnage_mechant).grid(row=5, column=0,
                                                                                                       padx=5, sticky=W)
        Label(self.cadre_caract_personnage_mechant, textvariable=self.defense_personnage_mechant).grid(row=6, column=0,
                                                                                                       padx=5, sticky=W)
        Label(self.cadre_caract_personnage_mechant, textvariable=self.intelligence_personnage_mechant).grid(row=7,
                                                                                                            column=0,
                                                                                                            padx=5,
                                                                                                            sticky=W)
        # cadre pour boutons du actions du Personnage
        self.cadre_boutons_personnage_mechant = Frame(self.cadre_personnage_mechant, width=350, height=140,
                                                      borderwidth=4,
                                                      relief=GROOVE)
        self.cadre_boutons_personnage_mechant.grid_propagate(False)
        self.cadre_boutons_personnage_mechant.grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky=W)

        # Bouton pour attaque du Personnage
        self.bouton_attaque_personnage_mechant = Button(self.cadre_boutons_personnage_mechant, text="Attaque",
                                                        command=self.attaque_de_personnage_mechant)
        self.bouton_attaque_personnage_mechant.grid(row=0, column=0, padx=5, sticky=W)
        self.bouton_perdre_sante_personnage_mechant = Button(self.cadre_boutons_personnage_mechant, text="Sante -5",
                                                             command=self.perdre_sante_personnage_mechant)
        self.bouton_perdre_sante_personnage_mechant.grid(row=0, column=1, padx=5, sticky=W)
        self.bouton_soigne_sante_personnage_mechant = Button(self.cadre_boutons_personnage_mechant, text="Sante +5",
                                                             command=self.soigne_sante_personnage_mechant)
        self.bouton_soigne_sante_personnage_mechant.grid(row=0, column=2, padx=5, sticky=W)

    def journal(self):
        self.cadre_journal = Frame(self.cadre_jeu_principal, width=380, height=440, borderwidth=4, relief=GROOVE)
        self.cadre_journal.grid_propagate(False)
        self.cadre_journal.grid(row=0, column=2, padx=5, pady=5)
        self.journal_text = Text(self.cadre_journal, width=42, height=25)
        scrollX = Scrollbar(self.cadre_journal, command=self.journal_text.xview, orient=HORIZONTAL)
        scrollX.grid(row=1, column=0, sticky='wes')
        scrollY = Scrollbar(self.cadre_journal, command=self.journal_text.yview, orient=VERTICAL)
        scrollY.grid(row=0, column=1, sticky='nse')
        self.journal_text.config(yscrollcommand=scrollY.set, xscrollcommand=scrollX.set)
        self.journal_text.grid_propagate(False)
        self.journal_text.grid(row=0, column=0, padx=5, pady=5)

    def add_photo(self, cadre, w, h, file_name):
        image = Image.open(file_name).resize((w, h), Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        label1 = Label(cadre, image=photo)
        label1.image = photo
        label1.place(x=0, y=0)

    def set_caracteristiques_personnage_gentil(self):
        self.race_personnage_gentil.set(f"Race : {self.personnage_gentil.race}")
        self.nom_personnage_gentil.set(f"Nom : {self.personnage_gentil.nom}")
        # if qui.sante <= 0:
        #     self.label_sante = self.sante_label.set(f"Sante : MORT")
        # else:
        self.label_sante_personnage_gentil = self.sante_personnage_gentil.set(
            f"Sante : {self.personnage_gentil.sante}")
        self.force_personnage_gentil.set(f"Force : {self.personnage_gentil.force}")
        self.endurance_personnage_gentil.set(f"Endurance : {self.personnage_gentil.endurance}")
        self.agilite_personnage_gentil.set(f"Agilite : {self.personnage_gentil.agilite}")
        self.defense_personnage_gentil.set(f"Defense : {self.personnage_gentil.defense}")
        self.intelligence_personnage_gentil.set(f"Intelligence : {self.personnage_gentil.intelligence}")

    def set_caracteristiques_personnage_mechant(self):
        self.race_personnage_mechant.set(f"Race : {self.personnage_mechant.race}")
        self.nom_personnage_mechant.set(f"Nom : {self.personnage_mechant.nom}")
        # if qui.sante <= 0:
        #     self.label_sante = self.sante_label.set(f"Sante : MORT")
        # else:
        self.label_sante_personnage_mechant = self.sante_personnage_mechant.set(
            f"Sante : {self.personnage_mechant.sante}")
        self.force_personnage_mechant.set(f"Force : {self.personnage_mechant.force}")
        self.endurance_personnage_mechant.set(f"Endurance : {self.personnage_mechant.endurance}")
        self.agilite_personnage_mechant.set(f"Agilite : {self.personnage_mechant.agilite}")
        self.defense_personnage_mechant.set(f"Defense : {self.personnage_mechant.defense}")
        self.intelligence_personnage_mechant.set(f"Intelligence : {self.personnage_mechant.intelligence}")

    def attaque_de_personnage_gentil(self):
        attaque = self.personnage_gentil.attaque(self.personnage_mechant)
        self.set_caracteristiques_personnage_gentil()
        self.set_caracteristiques_personnage_mechant()
        self.journal_text.insert(END, f"{attaque}\n")

    def attaque_de_personnage_mechant(self):
        attaque = self.personnage_mechant.attaque(self.personnage_gentil)
        self.set_caracteristiques_personnage_gentil()
        self.set_caracteristiques_personnage_mechant()
        self.journal_text.insert(END, f"{attaque}\n")

    def perdre_sante_personnage_gentil(self):
        action = self.personnage_gentil.perdre_sante(5)
        self.set_caracteristiques_personnage_gentil()
        self.journal_text.insert(END, f"{action}\n")

    def soigne_sante_personnage_gentil(self):
        action = self.personnage_gentil.gagne_sante(5)
        self.set_caracteristiques_personnage_gentil()
        self.journal_text.insert(END, f"{action}\n")

    def perdre_sante_personnage_mechant(self):
        action = self.personnage_mechant.perdre_sante(5)
        self.set_caracteristiques_personnage_mechant()
        self.journal_text.insert(END, f"{action}\n")

    def soigne_sante_personnage_mechant(self):
        action = self.personnage_mechant.gagne_sante(5)
        self.set_caracteristiques_personnage_mechant()
        self.journal_text.insert(END, f"{action}\n")

    def armure(self):
        if self.var_armure.get() == 1:
            action = Artefacts.utiliser_armure(self.personnage_gentil)
            self.set_caracteristiques_personnage_gentil()
            self.journal_text.insert(END, f"{action}\n")
        else:
            action = Artefacts.jeter_armure(self.personnage_gentil)
            self.set_caracteristiques_personnage_gentil()
            self.journal_text.insert(END, f"{action}\n")

    def epee(self):
        if self.var_epee.get() == 1:
            action = Artefacts.utiliser_epee(self.personnage_gentil)
            self.set_caracteristiques_personnage_gentil()
            self.journal_text.insert(END, f"{action}\n")
        else:
            action = Artefacts.jeter_epee(self.personnage_gentil)
            self.set_caracteristiques_personnage_gentil()
            self.journal_text.insert(END, f"{action}\n")

    def bottes(self):
        if self.var_bottes.get() == 1:
            action = Artefacts.utiliser_bottes(self.personnage_gentil)
            self.set_caracteristiques_personnage_gentil()
            self.journal_text.insert(END, f"{action}\n")
        else:
            action = Artefacts.jeter_bottes(self.personnage_gentil)
            self.set_caracteristiques_personnage_gentil()
            self.journal_text.insert(END, f"{action}\n")

    def autobataille(self):
        bataille = self.personnage_gentil.autobataille(self.personnage_mechant)
        self.set_caracteristiques_personnage_gentil()
        self.set_caracteristiques_personnage_mechant()
        self.journal_text.insert(END, f"{bataille}\n")


root = Tk()
app = Main(root)
root.geometry(TAILLE)

root.mainloop()
