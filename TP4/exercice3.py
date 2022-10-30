"""
exercice3.py
Description : Fonction softmax
Auteurs     : William Morin (2213763), Théo Manach (2058412)
"""

"""
Votre ami.e qui étudie en intelligence artificielle veut votre aide pour l'implémentation d'un outil qui lui sera très utile.

Vous devez programmer la fonction softmax: https://en.wikipedia.org/wiki/Softmax_function

L'utilisateur de votre programme doit entrer une série de nombres.
Par la suite, votre programme doit afficher le resultat de la fonction softmax pour chaque valeur.

Vous n'avez pas le droit d'utiliser la librairie Numpy.
* Note: Il n'est pas nécessaire de faire de la validation d'entrée.

### Exemple #1
Veuillez entrer une liste de nombres: 1 2 3 4 1 2 3
0.023640543021591385 0.06426165851049616 0.17468129859572226 0.4748329997443803 0.023640543021591385 0.06426165851049616 0.17468129859572226

### Exemple #2
Veuillez entrer une liste de nombres: -4 0 4
0.0003293204389638929 0.017980286735531547 0.9816903928255045

### Exemple #3
Veuillez entrer une liste de nombres: 0 0 0
0.3333333333333333 0.3333333333333333 0.3333333333333333

### Exemple #4
Veuillez entrer une liste de nombres: 1 0 1 0 1 0 1
0.19593864937345473 0.0720818008353937 0.19593864937345473 0.0720818008353937 0.19593864937345473 0.0720818008353937 0.19593864937345473

### Exemple #5
Veuillez entrer une liste de nombres: 14
1.0
"""

import math


# TODO: Commencez votre programme ici

def softmax(n: list):
    sum = 0.0

    for nombre in n:
        sum += math.exp(nombre)

    resultat = [math.exp(nombre) / sum for nombre in n]

    return resultat


liste = list(map(int, input("Veuillez entrer une liste de nombres: ").split()))

print(" ".join(map(str, softmax(liste))))
