grille = []
joueur1 = ''


def initialisation_de_grille():
    global grille
    for i in range(6):
        grille += [7 * [0]]
    return grille


def qui_comence_jeu():
    global joueur1
    tmp = ""
    while tmp not in ["1, 2"]:
        joueur1 = int(input("Quel joueur comence ?"))
        return joueur1


def joueur_choisit_colonne():
    tmp = ""
    while tmp not in ["1, 2, 3, 4, 5, 6, 7"]:
        colonne = int(input("Choisir le colonne ? 1, 2, 3, 4, 5, 6, 7"))
    return colonne


def jeton_tombe_dans_le_colonne(colonne):
    grille



# qui_comence_jeu()
print(*initialisation_de_grille(), sep='\n')
joueur_choisit_colonne()

