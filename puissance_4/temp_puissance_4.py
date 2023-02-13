LIGNES = 6
COLONNES = 7

grille = [COLONNES*[0] for _ in range(LIGNES)]
current_joueur = 1


def afficher_grille():
    """Metode pour afficher la grille"""
    # print(*grille, sep='\n')
    for i in range(len(grille)):
        print(grille[i])


def la_grille_pleine():
    plein = True
    for i in range(len(grille)):
        for j in range(i):
            if grille[i][j] != 0:
                plein = False
    return plein


def le_column_pleine():
    pass
    # plein = True
    # for i in range(len(grille)):
    #     for j in range(i):
    #         if grille[i][j] != 0:
    #             plein = False
    # return plein


def qui_comence_jeu():
    global joueur1
    tmp = ""
    while tmp not in ["1, 2"]:
        joueur1 = int(input("Quel joueur comence ? Entrez 1 pour ROUGE ou 2 pour BLUE"))
    return joueur1


# TODO: c'est possible choisir le 7 colonne     if grille[6 - i][colonne] == 0: # IndexError: list index out of range
def joueur_choisit_colonne():
    colonne = input("Choisir le colonne ? 1, 2, 3, 4, 5, 6, 7")
    # while colonne not in "1,2,3,4,5,6":
    #     print("Choisir le valeur correct.")
    #     colonne = input("Choisir le colonne ? 1, 2, 3, 4, 5, 6")
    return int(colonne) - 1


def jeton_tombe_dans_le_colonne(colonne, nouvelle_valeur):
    global grille
    for i in range(LIGNES):
        if grille[5 - i][colonne] == 0:
            grille[5 - i][colonne] = nouvelle_valeur
            break


def quatre_a_la_suite(joueur):

    # verifier les quatres horizontalement
    for c in range(COLONNES - 3):
        for l in range(LIGNES):
            if grille[l][c] == joueur and grille[l][c+1] == joueur and grille[l][c+2] == joueur and grille[l][c+3] == joueur:
                return True

    # verifier les quatres verticalement
    for c in range(COLONNES):
        for l in range(LIGNES - 3):
            if grille[l][c] == joueur and grille[l+1][c] == joueur and grille[l+2][c] == joueur and grille[l+3][c] == joueur:
                return True

    # verifier les quatres horizontalement positif
    for c in range(COLONNES - 3):
        for l in range(LIGNES - 3):
            if grille[l][c] == joueur and grille[l+1][c+1] == joueur and grille[l+2][c+2] == joueur and grille[l+3][c+3] == joueur:
                return True

    # verifier les quatres horizontalement negatif
    for c in range(COLONNES - 3):
        for l in range(LIGNES - 3):
            if grille[l][c] == joueur and grille[l-1][c-1] == joueur and grille[l-2][c-2] == joueur and grille[l-3][c-3] == joueur:
                return True

def changer_joueur():
    global current_joueur
    if current_joueur == 1:
        current_joueur = 2
    elif current_joueur == 2:
        current_joueur = 1


fin_de_jeu = False

while not fin_de_jeu:
    afficher_grille()
    print()
    print(f"Tour de joueur {current_joueur}")
    jeton_tombe_dans_le_colonne(joueur_choisit_colonne(), current_joueur)

    if quatre_a_la_suite(current_joueur):
        print(f"Joueur {current_joueur} gagné.")
        fin_de_jeu = True
        afficher_grille()
    # TODO: "Partie Nulle ! si le joueur gagné
    if la_grille_pleine() is False:
        print("Partie Nulle !")
    changer_joueur()
