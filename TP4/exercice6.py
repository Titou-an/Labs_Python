"""
exercice6.py
Description : Doublons dans une liste
Auteurs     : William Morin (2213763), Théo Manach (2058412)
"""

"""

Écrire un programme qui demande à l'utilisateur d'entrer plusieurs mots séparés d'un espace.

S'il y a seulement un doublon, afficher "Il y a 1 doublon".
S'il y a plus d'un doublon, afficher "Il y a x doublons", où x est le nombre de doublons.
S'il n'y a pas de doublons, afficher "Il n'y a pas de doublons".

* Note: Un mot est considéré comme un doublon s'il apparaît deux fois ou plus.

#### Exemples ####
* Note: Les phrases "* Explication: ..." ne devraient pas être affichées par votre programme. 
        Elles sont là pour vous aider à comprendre les exemples.

### Exemple 1
Entrer la liste: test test bonsoir poly
Il y a 1 doublon

### Exemple 2
Entrer la liste: test test bonsoir bonsoir mtl
Il y a 2 doublons
* Explication : Il y a en effet 2 doublons dans la liste ("test" et "bonsoir").

### Exemple 3 
Entrer la liste: poly mtl automne
Il n'y a pas de doublons

"""

# TODO: Commencez votre programme ici

liste = input("Entrer la liste: ").split()
doublons = set({})

for mot in liste:
    if mot not in doublons:
        if liste.count(mot) > 1:
            doublons.add(mot)

if len(doublons) == 0:
    print("Il n'y a pas de doublons")
elif len(doublons) == 1:
    print("Il y a 1 doublon")
else:
    print(f"Il y a {len(doublons)} doublons")