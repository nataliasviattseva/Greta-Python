from personnage import Personnage


class Artefacts(Personnage):
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
        Personnage.__init__(self, self.nom, self.sante, self.force, self.endurance, self.agilite, self.intelligence)
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

    def utiliser_epee(self):
        self.force = self.force * 2
        return f"Force de {self.nom} maintenant : {self.force}"

    def jeter_epee(self):
        self.force = int(self.force / 2)
        return f"Force de {self.nom} maintenant : {self.force}"

    def utiliser_armure(self):
        self.defense = self.defense * 2
        return f"Force de {self.nom} maintenant : {self.defense}"

    def jeter_armure(self):
        self.defense = int(self.defense / 2)
        return f"Force de {self.nom} maintenant : {self.defense}"

    def utiliser_bottes(self):
        self.agilite = self.agilite * 2
        return f"Force de {self.nom} maintenant : {self.agilite}"

    def jeter_bottes(self):
        self.agilite = int(self.agilite / 2)
        return f"Force de {self.nom} maintenant : {self.agilite}"
