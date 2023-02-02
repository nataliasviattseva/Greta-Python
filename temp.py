import random
# Genération de la liste aléatoire
liste_aleatoire = [random.randint(-5, 40) for _ in range(102)]
print(liste_aleatoire)

# stoker toutes les values negatives
negative = [i for i in liste_aleatoire if i < 0]
print(negative)

# autre option de genérer de la liste aléatoire
liste_aleatoire1 = []
for i in range(102):
    liste_aleatoire1.append(random.randint(-5, 40))
print(liste_aleatoire1)
