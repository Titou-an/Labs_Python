__version__ = "TP2 - Exercice #3"
__author__ = "William Morin (2213763), Théo Manach (2058412)"

# Écrire un programme qui calcule la plus petite distance euclidienne entre deux points par rapport à l’origine.
# Vous devez demander quatre valeurs à l'utilisateur, soit les points (x1, y1) et (x2, y2).
# Vous devez afficher la distance minimale avec deux chiffres après la virgule.
# Les points entrés par l'utilisateur peuvent avoir des décimales.

# Indice: La fonction min(a, b) vous donnera la valeur la plus petite entre "a" et "b".
# Exemple: 'min(3,1)' vous donnera 1.

"""
Exemple #1:
x1: 11
y1: 5
x2: -7
y2: 2
La distance minimale est de 7.28

Exemple #2:
x1: 6.53
y1: 2
x2: 9.87
y2: 0.4
La distance minimale est de 6.83
"""

# TODO: Commencez votre programme ici

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

distance1 = ((x1)**2 + (y1)**2)**0.5
distance2 = ((x2)**2 + (y2)**2)**0.5

print("La distance minimale est de", round(min(distance1,distance2),2))