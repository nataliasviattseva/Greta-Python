# ****************** #
## Lundi 13/02/2023 ##
# ****************** #

# début définition
class Personne:
    """Classe Personne"""


    # constructeur
    def __init__(self):
        # lister les champs
        self.nom = ""
        self.age = 0
        self.salaire = 0.0
    # fin constructeur


    # saisie des infos
    def saisie(self):
        self.nom = input("Nom : ")
        self.age = int(input("Age : "))
        self.salaire = int(input("Salaire : "))
    # fin saisie


    def affichage(self):
        print(f"Non : {self.nom}\nAge : {self.age}\nSalaire : {self.salaire}")


    # reste avant retraite
    def retraite(self, limite):
        reste = limite - int(self.age)
        if reste < 0:
            print(f"Vous êtes à la retraite")
        else:
            print(f"Il vous reste {reste}s années")
    # fin retraite


    def acces_par_numero(self):
        numero = int(input("№ ind. à traiter : "))
        if numero < len(liste):
            b = liste[numero]
            b.salaire *= 2
            print("xxx début affichage 2")
            for p in liste:
                print("%%%%%%%%%%%%")
                p.affichage()
        else:
            print("indice non valable")


# fin définition

# liste vide

liste = []

# nb. de pers ?
n = int(input("Nb de pers : "))

# saisie liste
for i in range(0, n):
    a = Personne()
    a.saisie()
    liste.append(a)

# affichage
for p in liste:
    print("----------------")
    p.affichage()

## ---------nouvelle page-----------
## appel du module
# import ModulePersonne as MP

## instanciation
# p = MP.Personne()
p = Personne()

# affichage tous les membres de p
print(dir(p))

## affectation aux champs
p.nom = input("Nom : ")
p.age = input("Age : ")
p.salaire = input("Salaire : ")

## affichage
print(f"Non : {p.nom}, Age : {p.age}, Salaire : {p.salaire}")

# saisie
p.saisie()

# méthode affichage
p.affichage()

# reste avant retraite
p.retraite(62)

a.acces_par_numero()
p.acces_par_numero()



class Voiture:


    def __init__(self, couleur, marque, roues, puissance):
        self.couleur = couleur
        self.marque = marque
        self.roues = roues
        self.puissance = puissance


    def affichage(self):
        print(f"-----------\nLa marque est : {self.marque}\nLe couleur: {self.couleur}\nNombre de roues: {self.roues}\nLa puissanc est {self.puissance} CH")


ferrari = Voiture(couleur="rouge", marque="ferrari", roues=4, puissance=450)
lamborgini = Voiture(couleur="blue", marque="lamborgini", roues=4, puissance=740)

ferrari.affichage()
lamborgini.affichage()


class Chiens:

    def __init__(self, nom, couleur, taille, jappe):
        self.nom = nom
        self.couleur = couleur
        self.taille = taille
        self.jappe = jappe

    def jappe_action(self):
        print("warf! warf!")

    def affichage(self):
        print(f"La couleur de {self.nom} est {self.couleur} et la taille est {self.taille}")
        if self.jappe is True:
            self.jappe_action()


chien_1 = Chiens(nom="Roxy", couleur="noir", taille="grande", jappe=True)
chien_2 = Chiens(nom="Mickey", couleur="gris", taille="petit", jappe=False)

chien_1.affichage()
chien_2.affichage()

# ****************** #
## Mardi 14/02/2023 ##
# ****************** #

class CompteBancaire:

    def __init__(self, nom='Dupont', solde=100):

        self.nom = nom
        self.solde = solde

    def depot(self, somme):
        """ajout d'une somme à l'atrubut solde"""
        self.solde += somme

    def solde_debit(self):
        if self.solde < 0:
            print("Alerte ! Le solde est negative")

    def retrait(self, somme):
        """retrait d'une somme à l'atrubut solde"""
        self.solde -= somme

    def affichage(self):
        """L'affichage des information d'un compte"""
        print(f"Le solde du compte bancaire de {self.nom} est {self.solde:.2f} euros")


compte_1 = CompteBancaire("Duchmol", 800)  # instanciation du compte_1
compte_1.depot(350)
compte_1.retrait(200)
compte_1.affichage()

compte_2 = CompteBancaire()  # instanciation du compte_1
compte_2.depot(-100)
compte_2.retrait(1000)
compte_2.solde_debit()
compte_2.affichage()

compte_3 = CompteBancaire("Natalia", 1000000)
compte_3.affichage()

class Compte:
    """Un exemple de class : gestion d'un compte bancaire"""

    # définition de la métode spéciale __init__
    def __init__(self, solde_initial):
        # assignation de l'atribut d'instance solde
        self.solde = float(solde_initial)

    # définition de la méthode nouveau_solde
    def nouveau_solde(self, somme):
        self.solde = float(somme)

    # définition de la méthode solde
    def solde(self):
        return self.solde

    # définition de la méthode credit
    def credit(self, somme):
        self.solde += somme
        return self.solde

    # définition de la méthode debit
    def debit(self, somme):
        self.solde -= somme
        return self.solde

    # définition de la méthode spéciale __add__ (surcharge de l'operateur +)
    def __add__(self, somme):
        """x.__add__(somme) <=> x + solde
        Crédite le compte de la valeur somme.
        Affiche 'Nouveau solde : somme'"""
        self.solde += somme
        print(f"Nouveau solde : {self.solde:.2f} euros.")
        return self

    # définition de la méthode spéciale __sub__ (surcharge de l'operateur -)
    def __sub__(self, somme):
        """x.__sub__(somme) <=> x - solde
        Débite le compte de la valeur somme.
        Affiche 'Nouveau solde : somme'"""
        self.solde -= somme
        print(f"Nouveau solde : {self.solde:.2f} euros.")
        return self


if __name__ == '__main__':
    """Ce bloc d'instructions est éxécuté si le module est lancé en tant que programme autonome
    Instanciation de l'objet cb1 de la classe Compte"""
    cb1 = Compte(1000)
    print("CB1 : ")
    print(cb1.solde)
    # print(cb1.solde())
    print(f"Solde : {cb1.solde:.2f}")
    print(f"Crédit : {cb1.credit(200):.2f}")
    print(f"Débit : {cb1.debit(50.23):.2f}")
    cb1.nouveau_solde(5100)
    print(f"Solde : {cb1.solde:.2f}")
    cb1 + 253.2
    cb1 - 1000 + 100
    cb1.__add__(500)
    cb1 - cb1.solde

    print("CB2 : ")
    cb2 = Compte(2000)
    print(f"Crédit : {cb2.credit(200):.2f}")
    print(f"Débit : {cb2.debit(150.80):.2f}")
    cb2.__add__(5000)
    cb2 + 500
    cb2 + cb2.solde
    print("BLABLA")
    # cb2 + cb2  # TypeError: unsupported operand type(s) for +=: 'float' and 'Compte'
    print(f"Solde : {cb2.solde:.2f}")
