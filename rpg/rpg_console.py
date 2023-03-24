class Personnage:

    def __init__(self, nom, vie, force, endurance, rapidite, intelligence):
        self.nom = nom
        self.vie = vie
        self.force = force
        self.endurance = endurance
        self.rapidite = rapidite
        self.intelligence = intelligence
        self.est_mort()

    # 4.3
    def est_mort(self):
        if self.vie > 0:
            return False
        else:
            return True

    # 4.4
    def affiche_etat(self):
        if self.est_mort():
            print(f"{self.nom} est mort !")
        else:
            print(f"Il reste {self.vie} points de vie du {self.nom}.")

    # 4.5
    def affiche_caracteristiques(self):
        print(f"""\n{self.nom} a :
        une force de {self.force}, 
        une endurance de {self.endurance}, 
        une rapidité de {self.rapidite},
        une intelligence de {self.intelligence}.\n""")

    # 4.6
    def perdre_vie(self, points_de_vie_perdus):
        print("________________perdre_vie_________________")
        self.vie -= points_de_vie_perdus
        print(f"{self.nom} subit une attaque, il perd {points_de_vie_perdus} points de vie.")
        print(f"Ses points de vies valent maintenant {self.vie}")
        if points_de_vie_perdus > self.vie:
            print("{self.nom} a subli une attaque mortelle !!!")

    # 4.7
    def gagne_vie(self, points_de_vie_gagne):
        print("_________________gagne_vie__________________")
        if not self.est_mort():
            self.vie += points_de_vie_gagne
            print(f"{self.nom} a été soigné. Ses points de vies valent maintenant {self.vie}")
        else:
            print(f"{self.nom} ne peut être soigné par ?Gandalf?, car {self.nom} est morte !")

    # 4.8
    def attaque(self, autre_personnage):
        print("__________________attaque___________________")
        if not self.est_mort() and not autre_personnage.est_mort():
            if not autre_personnage.esquive_attaque(self):  # autre_personnage.esquive == False
                self.points_de_degats = round(0.6 * self.force)
                print(f"points de degats : {self.points_de_degats}")
                autre_personnage.sante -= self.points_de_degats
        elif self.est_mort():
            print(f"{self.nom} ne peut attaque personne: il est morte !")
        elif autre_personnage.est_mort():
            print(f"{autre_personnage.nom} ne peut attaque personne: il est morte !")

    # 4.9
    def soigne(self, autre_personnage, points_de_soin):
        print("__________________soigne____________________")
        if not self.est_mort() and not autre_personnage.est_mort():
            autre_personnage.sante += points_de_soin
            print(f"{autre_personnage.nom} soigne {self.nom}.")
            print(f"{autre_personnage.nom} restature à {points_de_soin} de vie")
        elif autre_personnage.est_mort():
            print(f"{self.nom} ne peut pas soigner {autre_personnage.nom}")
            print(f"{autre_personnage.nom} est mort !!!")
        else:
            print(f"{autre_personnage.nom} ne peut pas soigner {self.nom}")
            print(f"{self.nom} est mort !!!")

    # 5.0
    def esquive_attaque(self, autre_personnage):
        print("_____________esquive_attaque________________")
        if not self.est_mort() and not autre_personnage.est_mort():
            rapidite_effectue = round(self.rapidite * 1.2)
            if rapidite_effectue > autre_personnage.force:
                print(f"{self.nom} esquive l'attaque de {autre_personnage.nom}")
                print(f"Esquive : calcul de rapidité de {self.nom} : {rapidite_effectue} contre {autre_personnage.force} pour la force de {autre_personnage.nom}")
                return True
            else:
                print(f"{autre_personnage.nom} attaque de {self.nom}")
                return False
        elif self.est_mort():
            print(f"{self.nom} ne peut esquiver de {autre_personnage.nom}. {self.nom} est mort !")
        else:
            print(f"{autre_personnage.nom} ne peut esquiver de {self.nom}. {autre_personnage.nom} est mort !")

    def se_deplace(self, points_de_deplacement):
        pass


class Magicien:

    def __init__(self):
        self.metier = "magicien"

    def faire_magie(self, points_de_magie):
        pass


class Human(Personnage, Magicien):

    def __init__(self):
        Personnage.__init__(self, self.nom, self.vie, self.force, self.endurance, self.rapidite, self.intelligence)
        Magicien.__init__(self)
        self.race = "Humain"


class Hobbit(Personnage, Magicien):

    def __init__(self):
        Personnage.__init__(self, self.nom, self.vie, self.force, self.endurance, self.rapidite, self.intelligence)
        Magicien.__init__(self)
        self.race = "Hobbit"


class Elfe(Personnage, Magicien):

    def __init__(self):
        Personnage.__init__(self, self.nom, self.vie, self.force, self.endurance, self.rapidite, self.intelligence)
        Magicien.__init__(self)
        self.race = "Elfe"


class Nain(Personnage, Magicien):

    def __init__(self):
        Personnage.__init__(self, self.nom, self.vie, self.force, self.endurance, self.rapidite, self.intelligence)
        Magicien.__init__(self)
        self.race = "Nain"


class Orque(Personnage, Magicien):

    def __init__(self):
        Personnage.__init__(self, self.nom, self.vie, self.force, self.endurance, self.rapidite, self.intelligence)
        Magicien.__init__(self)
        self.race = "Orque"


pers_1 = Personnage(nom="Bilbon Sacquet", vie=5, force=6, endurance=5, rapidite=1, intelligence=5)
pers_2 = Personnage(nom="Gollum", vie=5, force=5, endurance=5, rapidite=5, intelligence=5)
pers_3 = Personnage("Gandalf", 5, 5, 5, 5, 5)

pers_1.perdre_vie(1)
pers_1.affiche_etat()

pers_1.gagne_vie(2)
pers_1.affiche_etat()

pers_1.attaque(pers_2)
pers_1.affiche_etat()
pers_2.affiche_etat()

pers_1.soigne(pers_2, 3)
pers_1.affiche_etat()
pers_2.affiche_etat()

pers_1.esquive_attaque(pers_2)
pers_1.affiche_caracteristiques()
pers_2.affiche_caracteristiques()
pers_1.affiche_etat()
pers_2.affiche_etat()

pers_1.attaque(pers_2)
pers_1.affiche_etat()
pers_2.affiche_etat()

pers_2.gagne_vie(10)

pers_1.attaque(pers_2)
pers_1.affiche_etat()
pers_2.affiche_etat()

pers_1.soigne(pers_2, 10)

pers_1.attaque(pers_2)
pers_1.affiche_etat()
pers_2.affiche_etat()

pers_2 = Personnage(nom="Gollum", vie=10, force=5, endurance=5, rapidite=15, intelligence=5)

pers_1.attaque(pers_2)
pers_1.affiche_etat()
pers_2.affiche_etat()

pers_1.attaque(pers_2)
pers_1.affiche_etat()
pers_2.affiche_etat()

pers_2.attaque(pers_1)
pers_1.affiche_etat()
pers_2.affiche_etat()

pers_2.attaque(pers_1)
pers_1.affiche_etat()
pers_2.affiche_etat()


# pers_4 = Nain()
