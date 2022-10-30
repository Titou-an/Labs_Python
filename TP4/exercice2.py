"""
exercice2.py
Description : Cadeaux amis
Auteurs     : William Morin (2213763), Théo Manach (2058412)
"""

"""
Vous decidez de concevoir un programme pour vous aider a choisir des cadeaux pour vos amis

Vous demandez à 3 amis les cadeaux qu'ils aimeraient obtenir, separés par des espaces.
Ensuite, pour vous simplifier la tâche, vous decidez d'acheter seulement les cadeaux qui conviennent à vos 3 amis.

Votre programme doit afficher tous les cadeaux, separés par des espaces et en ordre alphabetique, que vos 3 amis ont en commun.

** Important: Vous DEVEZ résoudre cet exercice à l'aide d'ensembles ("set") et de leurs propriétées.
** Note: Votre programme ne devrait pas être sensible à la lettre majuscule.

### Exemple #1:

Cadeau idéal pour ton ami 1: casquette avion chandail bateau 
Cadeau idéal pour ton ami 2: bateau pantalon avion casquette
Cadeau idéal pour ton ami 3: casquette avion bateau lunette
avion bateau casquette

### Exemple #2:

Cadeau idéal pour ton ami 1: casquette avion chandail
Cadeau idéal pour ton ami 2: lunette
Cadeau idéal pour ton ami 3: lunette

### Exemple #3:

Cadeau idéal pour ton ami 1: oiseau chandail
Cadeau idéal pour ton ami 2: oiseau origami
Cadeau idéal pour ton ami 3: oiseau bas
oiseau

### Exemple #4:

Cadeau idéal pour ton ami 1: chandail oiseau
Cadeau idéal pour ton ami 2: origami oiseau
Cadeau idéal pour ton ami 3: bas oiseau
oiseau

"""
# TODO: Commencez votre programme ici

cadeaux1 = set(input("Cadeau idéal pour ton ami 1: ").casefold().split())
cadeaux2 = set(input("Cadeau idéal pour ton ami 2: ").casefold().split())
cadeaux3 = set(input("Cadeau idéal pour ton ami 3: ").casefold().split())

intersection = list(cadeaux1.intersection(cadeaux2,cadeaux3))
intersection.sort()
print(" ".join(intersection))






