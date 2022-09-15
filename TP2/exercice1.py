__version__ = "TP2 - Exercice #1"
__author__ = "William Morin (2213763), Théo Manach (2058412)"

# Vous devez écrire un programme qui demande à l'utilisateur un nombre entier
# et qui calcule le resultat de l'equation n + nn + nnn. Voir exemples ci-dessous.
# Vous n'avez pas le droit d'utiliser l'opération mathématique de mutliplication. 

"""
Exemple 1:
Veuillez entrer un entier: 5
Le resultat est : 155

Exemple 2:
Veuillez entrer un entier: 1
Le résultat est : 3
"""

# TODO: Commencez votre programme ici

n = int(input("Veuillez entrer un entier: "))
resultat =  n + (n * n) + (n * n * n)
print("Le résultat est :", resultat)