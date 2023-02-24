from personnage import *


class Artefacts:
    # épée +force
    # armure +defence
    # bottes +esquive ???
    # 3 silmatils +100 sante ou + vie (si le personnage est mort)
    # 19 anneaux:
    #  chaqun pour characteristiques
    # peut-etre on ne peut modifier le karma

    def __init__(self,
                 epee,
                 armure,
                 bottes,
                 silmaril,
                 anneau_sante,
                 anneau_force,
                 anneau_endurance,
                 anneau_agilite,
                 anneau_defence,
                 anneau_intelligence,
                 anneau_magie,
                 anneau_karma):

        self.epee = epee
        self.armure = armure
        self.bottes = bottes
        self.silmaril = silmaril
        self.anneau_sante = anneau_sante
        self.anneau_force = anneau_force
        self.anneau_endurance = anneau_endurance
        self.anneau_agilite = anneau_agilite
        self.anneau_defence = anneau_defence
        self.anneau_intelligence = anneau_intelligence
        self.anneau_magie = anneau_magie
        self.anneau_karma = anneau_karma

    # def apliquier_epee(self):
    #     self.forte_modifie = self.force + 5
    #     return self.forte_modifie

