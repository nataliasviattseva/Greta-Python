grille = [6*[0] for _ in range(7)]
current_joueur = 1


def afficher_grille():
    # global grille
    for i in range(7):
        print(grille[i])


def la_grille_pleine():
    plein = True
    for i in range(7):
        for j in range(6):
            if grille[i][j] != 0:
                plein = False
    return plein


def qui_comence_jeu():
    global joueur1
    tmp = ""
    while tmp not in ["1, 2"]:
        joueur1 = int(input("Quel joueur comence ? Entrez 1 pour ROUGE ou 2 pour BLUE"))
    return joueur1

# TODO: c'est possible choisir le 7 colonne     if grille[6 - i][colonne] == 0: # IndexError: list index out of range
def joueur_choisit_colonne():
    tmp = ""
    while tmp not in ['1,2,3,4,5,6']:
        return int(input("Choisir le colonne ? 1, 2, 3, 4, 5, 6")) - 1



def jeton_tombe_dans_le_colonne(colonne, nouvelle_valeur):
    for i in range(7):
        if grille[6 - i][colonne] == 0:
            grille[6 - i][colonne] = nouvelle_valeur
            break


def changer_joueur():
    global current_joueur
    if current_joueur == 1:
        current_joueur = 2
    elif current_joueur == 2:
        current_joueur = 1


continue_le_jeu = True

while continue_le_jeu:
    afficher_grille()
    print(f"Tour de joueur {current_joueur}")
    jeton_tombe_dans_le_colonne(joueur_choisit_colonne(), current_joueur)
    afficher_grille()
    changer_joueur()
    print()
    # continue_le_jeu = la_grille_pleine()
