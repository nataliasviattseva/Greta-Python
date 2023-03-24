from races import *

frodon = Hobbit(nom="Frodon Sacquet",
                    sante=100,
                    force=100,
                    endurance=100,
                    agilite=100,
                    defense=100,
                    intelligence=100,
                    magie=100,
                    karma=100)

gandalf_le_gris = Ainur(nom="Gandalf le Gris",
                        sante=101,
                        force=101,
                        endurance=101,
                        agilite=101,
                        defense=101,
                        intelligence=101,
                        magie=101,
                        karma=101)

samsagace_gamegie = Hobbit(nom="Samsagace Gamegie",
                           sante=200,
                           force=200,
                           endurance=200,
                           agilite=200,
                           defense=200,
                           intelligence=200,
                           magie=200,
                           karma=200)

aragorn = Homme(nom="Aragorn",
                sante=5,
                force=5,
                endurance=5,
                agilite=5,
                defense=5,
                intelligence=5,
                magie=5,
                karma=5)

legolas = Elfe(nom="Legolas",
               sante=1,
               force=1,
               endurance=1,
               agilite=1,
               defense=1,
               intelligence=1,
               magie=1,
               karma=1)

sauron = Ainur(nom="Sauron",
               sante=55,
               force=5,
               endurance=5,
               agilite=5,
               defense=5,
               intelligence=5,
               magie=5,
               karma=5)

sauron1 = Ainur(nom="Sauron111",
               sante=15,
               force=15,
               endurance=15,
               agilite=15,
               defense=15,
               intelligence=15,
               magie=15,
               karma=15)

liste_personnages = [["frodon", frodon, f"images\\frodon_sacquet.png"],
                     ["gandalf", gandalf_le_gris, f"images\\gandalf.png"],
                     ["sam", samsagace_gamegie, f"images\\sam.png"],
                     ["aragorn", aragorn, f"images\\aragorn.png"],
                     ["legolas", legolas, f"images\\legolas.png"]]

liste_ennemis = [["sauron", sauron, f"images\\sauron.png"],
                 ["sauron1111", sauron, f"images\\sauron.png"]]
