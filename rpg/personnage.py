from artefacts import *


class Personnage():

    # initialisation le constructor de la classe Personnage avec caractéristiques principals
    def __init__(self,
                 nom,
                 sante,
                 force,
                 endurance,
                 agilite,
                 defence,
                 intelligence,
                 magie,
                 karma):

        self.nom = nom
        self.sante = sante
        self.force = force
        self.endurance = endurance
        self.agilite = agilite
        self.defense = defence
        self.intelligence = intelligence
        self.magie = magie
        self.karma = karma
        self.est_mort()

    # méthode pour vérifier si un personnage est vivant
    def est_mort(self):
        if self.sante > 0:
            return False
        else:
            return True

    # 4.4
    # def affiche_etat(self):
    #     if self.est_mort():
    #         print(f"{self.nom} est mort !")
    #     else:
    #         print(f"Il reste {self.sante} points de sante du {self.nom}.")

    # 4.5
    # def affiche_caracteristiques(self):
    #     print(f"""\n{self.nom} a :
    #     une force de {self.force},
    #     une endurance de {self.endurance},
    #     une agilite de {self.agilite},
    #     une intelligence de {self.intelligence}.\n""")

    # 4.6
    def perdre_sante(self, points_de_sante_perdus):
        self.sante -= points_de_sante_perdus
        if points_de_sante_perdus > self.sante:
            return f"{self.nom} a subli une attaque mortelle !!!"
        else:
            return f"{self.nom} subit une attaque, il perd {points_de_sante_perdus} points de sante.\nSes points de sante valent maintenant {self.sante}"

    # 4.7
    def gagne_sante(self, points_de_sante_gagne):
        print("_________________gagne_sante__________________")
        if not self.est_mort():
            self.sante += points_de_sante_gagne
            print(f"{self.nom} a été soigné. Ses points de santes valent maintenant {self.sante}")
        else:
            print(f"{self.nom} ne peut être soigné par ?Gandalf?, car {self.nom} est morte !")

    # 4.8
    def attaque(self, autre_personnage):
        if not self.est_mort() and not autre_personnage.est_mort():
            if not autre_personnage.esquive_attaque(self):  # autre_personnage.esquive == False
                self.points_de_degats = round(0.6 * self.force)
                autre_personnage.sante -= self.points_de_degats
                return f"points de degats : {self.points_de_degats}"
        elif self.est_mort():
            return f"{self.nom} ne peut attaque personne: il est morte !"
        elif autre_personnage.est_mort():
            return f"{autre_personnage.nom} ne peut attaque personne: il est morte !"

    # 4.9
    def soigne(self, autre_personnage, points_de_soin):
        print("__________________soigne____________________")
        if not self.est_mort() and not autre_personnage.est_mort():
            autre_personnage.sante += points_de_soin
            print(f"{autre_personnage.nom} soigne {self.nom}.")
            print(f"{autre_personnage.nom} restature à {points_de_soin} de sante")
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
            agilite_effectue = round(self.agilite * 1.2)
            if agilite_effectue > autre_personnage.force:
                print(f"{self.nom} esquive l'attaque de {autre_personnage.nom}")
                print(f"Esquive : calcul de agilité de {self.nom} : {agilite_effectue} contre {autre_personnage.force} pour la force de {autre_personnage.nom}")
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


