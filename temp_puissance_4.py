grille = []
joueur1 = ''


def initialisation_de_grille():
    global grille
    for i in range(6):
        grille += [7 * [0]]
    return grille


def qui_comence_jeux():
    global joueur1
    tmp = ""
    while tmp not in ["1, 2"]:
        joueur1 = int(input("Quel joueur comence ?"))
        return joueur1

qui_comence_jeux()
print(*initialisation_de_grille(), sep='\n')

