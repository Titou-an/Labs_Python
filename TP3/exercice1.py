__version__ = "TP3 - Exercice #1"
__author__ = "William Morin (2213763), Théo Manach (2058412)"

"""
Écrire un programme qui demande à l'utilisateur d'entrer un nombre entier n
et qui affiche les n premiers nombres de la suite de Fibonacci.
On vous demande également de faire de la validation d'entrée.
Le nombre n devrait être un nombre entier strictement positif (1, 2, 3, …).
Suite de Fibonacci : https://fr.wikipedia.org/wiki/Suite_de_Fibonacci
Indice : Pensez à la fonction isdigit() pour la validation d'entrée
========================================= Exemple 1 =========================================
$ python3 exercice1.py
Veuillez entrer le nombre n (nombre entier positif) : 4
La serie recherchee est : 0 1 1 2
========================================= Exemple 2 =========================================
$ python3 exercice1.py
Veuillez entrer le nombre n (nombre entier positif) : -1
Veuillez entrer le nombre n (nombre entier positif) : 0
Veuillez entrer le nombre n (nombre entier positif) : 10
La serie recherchee est : 0 1 1 2 3 5 8 13 21 34
"""

# TODO : Ajouter votre code

phi = (1+5**0.5)/2

while True:
    inp = input("Veuillez entrer le nombre n (nombre entier positif) :")
    if inp.isnumeric():
        n = int(inp)
        if n > 0:
            break

precedant = 0
suivant = 1
resultat = [0,1]

for i in range(2, n):
    nouveau = suivant + precedant
    resultat.append(nouveau)
    precedant = suivant
    suivant = nouveau

print("La serie recherchee est :", end=" ")
for nombre in range(n):
    print(resultat[nombre], end=" ")
