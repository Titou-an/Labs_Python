__version__ = "TP3 - Exercice #5"
__author__ = "Nom eleve 1 (matricule 1), nom eleve 2 (matricule 2)"

"""
Écrire un programme qui affiche dans la fenêtre du terminal un losange régulier
ayant la forme d'un diamant connaissant sa demi-diagonale.
Vous devez également faire de la validation d'entrée.
La demi-diagonale doit être un entier strictement positif (c'est à dire > 0).
Note : Si on représente la sortie du terminal comme un grille,
chaque caractère occupe exactement une case et la distance entre deux cases
adjacentes vaut l'unité. Sur l'exemple suivant, vous pourrez remarquer
que partant du centre et allant vers n'importe quel direction
(haut, bas, gauche ou droite) on a exactement un nombre de caractères
étant la demi-diagonale.
===================================== Exemple ====================================
$ python3 exercice5.py
Veuillez entrer la valeur de la demi-diagonale (nombre entier strictement positif) : 5
.....@.....
....@@@....
...@@@@@...
..@@@@@@@..
.@@@@@@@@@.
@@@@@@@@@@@
.@@@@@@@@@.
..@@@@@@@..
...@@@@@...
....@@@....
.....@.....
"""

# TODO : Ajouter votre code

while True:
    inp = input("Veuillez entrer la valeur de la demi-diagonale (nombre entier strictement positif) :")
    if inp.isnumeric():
        d = int(inp)
        if d > 0:
            break

for y in range(d + 1):
    for x in range(2 * d + 1):
        if d - y <= x <= d + y:
            print("@", end="")
        else:
            print(".", end="")
    print()

for y in range(d, 0, -1):
    for x in range(2 * d + 1):
        if d - y < x < d + y:
            print("@", end="")
        else:
            print(".", end="")

    print()
