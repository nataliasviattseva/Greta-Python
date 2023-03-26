class Personnage:

    # initialisation le constructor de la classe Personnage avec caractéristiques principals
    def __init__(self,
                 nom,
                 sante,
                 force,
                 endurance,
                 agilite,
                 defence,
                 intelligence):

        self.nom = nom
        self.sante = sante
        self.force = force
        self.endurance = endurance
        self.agilite = agilite
        self.defense = defence
        self.intelligence = intelligence
        self.est_mort()
        self.esquive = False

    # méthode pour vérifier si un personnage est vivant
    def est_mort(self):
        if self.sante > 0:
            return False
        else:
            return True

    def perdre_sante(self, points_de_sante_perdus):
        self.sante -= points_de_sante_perdus
        if points_de_sante_perdus > self.sante:
            return f"{self.nom} a subli une attaque mortelle !!!"
        else:
            return f"{self.nom} subit une attaque, il perd {points_de_sante_perdus} points de sante.\nSes points de sante valent maintenant {self.sante}"

    def gagne_sante(self, points_de_sante_gagne):
        if not self.est_mort():
            self.sante += points_de_sante_gagne
            return f"{self.nom} a été soigné. Ses points de santes valent maintenant {self.sante}"
        else:
            return f"{self.nom} ne peut être soigné par ? {self.nom}, car {self.nom} est morte !"

    def attaque(self, autre_personnage):
        if not self.est_mort() and not autre_personnage.est_mort():
            if autre_personnage.esquive == False:
                self.points_de_degats = round(0.6 * self.force)
                autre_personnage.sante -= self.points_de_degats
                return f"""{self.nom} attaque {autre_personnage.nom}.
Points de degats (0.6 * {self.force}) : {self.points_de_degats}.
Sante de {self.nom}: {self.sante}.
Sante de {autre_personnage.nom}: {autre_personnage.sante}"""
        elif self.est_mort():
            return f"{self.nom} ne peut attaque personne: il est morte !"
        elif autre_personnage.est_mort():
            return f"{self.nom} ne peut attaque {autre_personnage.nom}: il est morte !"

    def soigne(self, autre_personnage, points_de_soin):
        if not self.est_mort() and not autre_personnage.est_mort():
            autre_personnage.sante += points_de_soin
            return f"""{autre_personnage.nom} soigne {self.nom}."/n
{autre_personnage.nom} restature à {points_de_soin} de sante"""
        elif autre_personnage.est_mort():
            return f"""{self.nom} ne peut pas soigner {autre_personnage.nom}"/n
            {autre_personnage.nom} est mort !!!"""
        else:
            return f"""{autre_personnage.nom} ne peut pas soigner {self.nom}"/n
            {self.nom} est mort !!!"""

    def esquive_attaque(self, autre_personnage):
        if not self.est_mort() and not autre_personnage.est_mort():
            agilite_effectue = round(self.agilite * 1.2)
            agilite_effectue = round(self.agilite * 1.2)
            if agilite_effectue > autre_personnage.force:
                self.esquive = True
                return f"""{self.nom} esquive l'attaque de {autre_personnage.nom}.
Esquive : calcul de agilité de {self.nom} : {agilite_effectue} contre {autre_personnage.force} pour la force de {autre_personnage.nom}"""
            else:
                self.esquive = False
                return f"{autre_personnage.nom} attaque de {self.nom}"
        elif self.est_mort():
            return f"{self.nom} ne peut esquiver de {autre_personnage.nom}. {self.nom} est mort !"
        else:
            return f"{autre_personnage.nom} ne peut esquiver de {self.nom}. {autre_personnage.nom} est mort !"

    def se_deplace(self, points_de_deplacement):
        pass

    def autobataille(self, autre_personnage):
        liste = []
        while True:
            turn = 0
            if not self.est_mort() and not autre_personnage.est_mort():
                if turn == 0 and not autre_personnage.est_mort():
                    autre_personnage.attaque(self)
                    turn = 1
                    liste.append(f"{autre_personnage.nom} attaque !\n{self.nom} sante est {self.sante}\n")
                if turn == 1 and not self.est_mort():
                    self.attaque(autre_personnage)
                    liste.append(f"{self.nom} attaque ! \n{autre_personnage.nom} sante est {autre_personnage.sante}\n")
            else:
                liste.append(f"{self.nom} or {autre_personnage.nom} est mort !\n")
                break
        return '\n'.join(liste)
