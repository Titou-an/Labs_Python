"""
exercice5.py
Description : Somme des index des doublons.
Auteurs     : William Morin (2213763), Théo Manach (2058412)
"""

"""
Écrire un programme qui demande à l'utilisateur d'entrer une liste de nombres et qui demande aussi
à l'utilisateur d'entrer un nombre k.
Le programme doit chercher dans cette liste s'il y'a des doublons tels que la somme de leurs indexes 
est strictement supérieure à k.


* Note : Il se peut qu'il y ait un nombre qui apparait plus de 2 fois, il faut alors faire la sommes des
deux PLUS GRANDS index.
* Note: Si plusieurs nombres respectent les conditions, il faut afficher seulement le premier nombre qui apparaît. 
        Voir exemple #5 ci-dessous.

* Note: Il n'est pas nécessaire de faire de la validation d'entrée.

#### Exemples ####
* Note: Les phrases "* Explication: ..." ne devraient pas être affichées par votre programme. 
        Elles sont là pour vous aider à comprendre les exemples.

### Exemple 1:
Veuillez entrer une liste de nombres: 1 2 3 4 5 1
Veuillez entrer le nombre k: 3
1 est un doublon dans la liste et la somme des index est supérieure à 3

* Explication: On voit qu'il y a effectivement le nombre 1 qui apparait 2 fois.
* Explication: Le premier "1" est à l'index 0 et le deuxieme est à l'index 5. ==> 0 + 5 = 5. Et 5 > 3.

### Exemple 2:
Veuillez entrer une liste de nombres: 1 1 2 3 4
Veuillez entrer le nombre k: 5
Il n'y a pas de doublons tels la somme des index est supérieure à 5

* Explication: On voit qu'il y a effectivement le nombre 1 qui apparait 2 fois.
* Explication: Or, la somme des index (0 et 1) est inférieure à k (1 < 5).

### Exemple 3:
Veuillez entrer une liste de nombres: 1 2 3 4 5
Veuillez entrer le nombre k: 2
Il n'y a pas de doublons tels la somme des index est supérieure à 2

* Explication: Il n'y a pas de doublons dans la liste.

### Exemple 4:
Veuillez entrer une liste de nombres: 9 18 0 14 18 7 4 8 29 81 18
Veuillez entrer le nombre k: 7
18 est un doublon dans la liste et la somme des index est supérieure à 7

* Explication: Le nombre "18" apparaît trois fois, soit aux indices 1, 4 et 10.
* Explication: Si l'on garde seulement les deux plus grands indices, soit 4 et 10, on arrive à une somme (14) supérieure à 7.

### Exemple 5:
Veuillez entrer une liste de nombres: 1 2 1 2 1
Veuillez entrer le nombre k: 2
{1: [0, 2, 4], 2: [1, 3]}
1 est un doublon dans la liste et la somme des index est supérieure à 2

* Explication: Le nombre "1" apparaît trois fois, soit aux indices 0, 2 et 4. Somme: 6
* Explication: Le nombre "2" apparaît deux fois, soit aux indices 1 et 3. Somme: 4
* Explication: Pour k=2, ces deux nombres respectent les conditions. Or, le nombre "1" apparaît en premier dans la liste de nombres.
* Explication: C'est donc celui-là qu'on affiche dans la phrase en sortie de programme.
"""

# TODO: Commencez votre programme ici

liste = list(map(int, input("Veuillez entrer une liste de nombres: ").split()))
k = int(input("Veuillez entrer le nombre k: "))
doublons = {}
resultat = None

for i in range(len(liste)):
    if liste[i] not in doublons.keys():
        if liste.count(liste[i]) > 1:
            doublons[liste[i]] = []
            for j in range(i, len(liste)):
                if liste[i] == liste[j]:
                    doublons[liste[i]].append(j)

for doublon, index in doublons.items():
    if index[-1] + index[-2] > k :
        resultat = doublon
        break
        
if resultat == None:
    print(f"Il n'y a pas de doublons tels la somme des index est supérieure à {k}")
else:
    print(f"{resultat} est un doublon dans la liste et la somme des index est supérieure à {k}")
