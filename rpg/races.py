from personnage import Personnage


class Homme(Personnage):

    def __init__(self):
        Personnage.__init__(self, self.nom, self.sante, self.force, self.endurance, self.agilité, self.intelligence)
        self.race = "Humain"


class Hobbit(Personnage):

    def __init__(self, nom, sante, force, endurance, agilite, defense, intelligence, magie, karma):
        Personnage.__init__(self,
                            nom,
                            sante,
                            force,
                            endurance,
                            agilite,
                            defense,
                            intelligence,
                            magie,
                            karma)

        self.race = "Hobbit"



class Elfe(Personnage):

    def __init__(self):
        Personnage.__init__(self, self.nom, self.sante, self.force, self.endurance, self.agilité, self.intelligence)
        self.race = "Elfe"


class Nain(Personnage):

    def __init__(self):
        Personnage.__init__(self, self.nom, self.sante, self.force, self.endurance, self.agilité, self.intelligence)
        self.race = "Nain"


class Orque(Personnage):

    def __init__(self):
        Personnage.__init__(self, self.nom, self.sante, self.force, self.endurance, self.agilite, self.intelligence)
        self.race = "Orque"


class Ainur(Personnage):

    def __init__(self, nom, sante, force, endurance, agilite, defense, intelligence, magie, karma):
        Personnage.__init__(self,
                            nom,
                            sante,
                            force,
                            endurance,
                            agilite,
                            defense,
                            intelligence,
                            magie,
                            karma)
        self.race = "Ainur"