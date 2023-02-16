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


from tkinter import *


class EnterMessage(Frame):
    """Classe EnterMessage  (Frame de saisie du message)
    Cette classe dérive de la classe Tkinter.Frame"""

    def __init__(self, master=None):
        """Initialisation : création d'un widget Frame"""
        Frame.__init__(self, master, bg='navy')
        self.pack(padx=10, pady=10)
        self.CreateWidgets()

    def CreateWidgets(self):
        """Création des widgets Entry et Button dans le widget Frame"""
        self.NouveauMessage = StringVar()
        Entry(master=self, textvariable=self.NouveauMessage).pack(side=LEFT, padx=10, pady=10)
        Button(master=self, text="Nouveau", fg="navy", command=self.nouveau).pack(padx=10, pady=10)

    def nouveau(self):
        """Création d'une instance de la classe NewPostIt"""
        if self.NouveauMessage.get() != "":
            NewPostIt(master=self.master, message=self.NouveauMessage.get())
            self.NouveauMessage.set("")


class NewPostIt(Frame):
    """Classe post-it (Frame Post-It)
    Cette classe dérive de la classe Tkinter.Frame"""

    def __init__(self, master=None, message=None):
        """Initialisation : création d'un widget Frame"""
        Frame.__init__(self, master, bg='grey')
        self.pack(side=LEFT, padx=10, pady=10)
        self.CreateWidgets(message)

    def CreateWidgets(self, message):
        """Création des widgets Label et Button dans le widget Frame"""
        Label(master=self, text=message, fg="maroon", bg='white').pack(padx=10, pady=10)
        Button(master=self, text="Effacer", fg="navy", command=self.destroy).pack(padx=10, pady=10)


if __name__ == '__main__':
    # création de la fenêtre principale
    mafenetre = Tk()
    mafenetre.title("Post-it")

    mafenetre['bg'] = "blue"

    # Création d'une instance de la classe EnterMessage
    EnterMessage(master=mafenetre)

    mafenetre.mainloop()


# ****************** #
## Jeudi 16/02/2023 ##
# ****************** #

import string


class Alphabet_majuscules(object):
    # classe mère

    def __init__(self):
        self.lettres_maj = string.ascii_uppercase
        # équivalent à une chaine reprenant tout l'alphabet avec la métode upper()
        # ou plus simplement une chaîne avec tout l'alphabet en majuscules


class Alphabet_minuscules(Alphabet_majuscules):
    # classe fille

    def __init__(self):
        Alphabet_majuscules.__init__(self)
        self.lettres_min = self.lettres_maj.lower()


class Alphabet_tri(Alphabet_minuscules):
    # classe petite-fille

    def __init__(self):
        Alphabet_minuscules.__init__(self)
        self.voyelles = []
        self.consonnes = []
        self.voyelles_maj = []
        self.consonnes_maj = []
        for lettre in self.lettres_min:
            if lettre in "aeiouy":
                self.voyelles.append(lettre)
            else:
                self.consonnes.append(lettre)
        for lettre in self.lettres_maj:
            if lettre in "AEIOUY":
                self.voyelles_maj.append(lettre)
            else:
                self.consonnes_maj.append(lettre)

    def listes_vers_chaines(self):
        self.voyelles_chaine = "".join(self.voyelles)
        self.consonnes_chaine = "".join(self.consonnes)
        self.voyelles_chaine_maj = "".join(self.voyelles_maj)
        self.consonnes_chaine_maj = "".join(self.consonnes_maj)

    def voyelles_maj_my(self):
        return [x.upper() for x in self.voyelles]

    def consonnes_maj_my(self):
        return [x.upper() for x in self.consonnes]


test_1 = Alphabet_majuscules()
print(f"test_1.lettres_maj : {test_1.lettres_maj}")

test_2 = Alphabet_minuscules()
print(f"test_2.lettres_maj : {test_2.lettres_maj}")
print(f"test_2.lettres_min : {test_2.lettres_min}")

test_3 = Alphabet_tri()
print(f"test_3.voyelles : {test_3.voyelles}")
print(f"test_3.consonnes : {test_3.consonnes}")
test_3.listes_vers_chaines() # il faut appeler le method avant
print(f"test_3.listes_vers_chaines : {test_3.listes_vers_chaines}")
print(f"test_3.voyelles_chaine : {test_3.voyelles_chaine}")
print(f"test_3.consonnes_chaine : {test_3.consonnes_chaine}")
print(f"test_3.voyelles_chaine_maj : {test_3.voyelles_chaine_maj}")
print(f"test_3.consonnes_chaine_maj : {test_3.consonnes_chaine_maj}")
print(f"test_3.voyelles_maj : {test_3.voyelles_maj}")
print(f"test_3.consonnes_maj : {test_3.consonnes_maj}")
print(f"test_3.voyelles_maj_my() : {test_3.voyelles_maj_my()}")
print(f"consonnes_maj_my() : {test_3.consonnes_maj_my()}")

class Voiture:
    """Classe représentant une voiture"""

    def __init__(self):
        """Constructeur de notre class"""

        self.nombre_roues = 4
        self.nombre_fauteuils = 1
        self.moteur = "propulsion"

        """méthode"""

"""Création de l'objet"""
ma_voiture = Voiture()

print(ma_voiture.moteur)
print(ma_voiture.nombre_roues)
print(ma_voiture.nombre_fauteuils)


class Citroen:

    def __init__(self):

        self.type_suspension = "Hydractives"
        self.logo = "Chevrons"
        self.marque = "Citroen"
        self.couleur = "orange"


ma_citroen = Citroen()

print(ma_citroen.type_suspension)
print(ma_citroen.logo)
print(ma_citroen.marque)


class BondBug(Voiture):

    def __init__(self):
        """Héritage de la classe Voiture()"""
        Voiture.__init__(self)
        self.marque = "Bond"
        self.modele = "Bug"
        self.nombre_roues = 3
        self.nombre_fauteuils = 2


ma_bug = BondBug()

print(ma_bug.marque)
print(ma_bug.moteur)
print(ma_bug.nombre_roues)
print(ma_bug.nombre_fauteuils)


"""Tests d'héritage"""
class CitroenDs(Voiture, Citroen):

    def __init__(self):
        Voiture.__init__(self)
        Citroen.__init__(self)
        self.modele = "DS de 1967"
        self.couleur = "rouge"

ma_super_DS = CitroenDs()

print(ma_super_DS.nombre_roues)
print(ma_super_DS.logo)
print(ma_super_DS.marque)
print(ma_super_DS.couleur)

print(ma_citroen.couleur)
