"""
exercice9.py
Description : Professeurs de projet 1 ou 2
Auteurs     : William Morin (2213763), Théo Manach (2058412)
"""

"""
Écrire un programme qui demande aux utilisateurs d'entrer deux listes différentes, la première étant
la liste des professeurs qui enseignent le cours de projet intégrateur #1 
et la deuxième est celle des professeurs qui enseignent le projet intégrateur #2.
Le programme doit afficher les professeurs qui enseignent qu'un seul des deux projets. 
Il faut ensuite trier ces professeurs par ordre alphabetique.

* Indice: utilisez les ensembles et leurs propriétés.

* Note: Votre programme doit être sensible à la lettre majuscule. Par exemple, "Stephane" et "stephane" ne sont pas identiques pour les fins de cet exercice.

### Exemple 1:

Veuillez entrer la liste des professeurs de projet 1: Francois Jean Martin Stephane Alexandre Joseph
Veuillez entrer la liste des professeurs de projet 2: Francois Mike Martin Stephane Claude Jacques
Les professeurs suivants enseignent un seul des deux projets:  ['Alexandre', 'Claude', 'Jacques', 'Jean', 'Joseph', 'Mike']

### Exemple 2:

Veuillez entrer la liste des professeurs de projet 1: Francois Jean Martin Stephane Alexandre Joseph
Veuillez entrer la liste des professeurs de projet 2: Francois Jean Martin Stephane Alexandre
Joseph est le seul professeur qui enseigne un seul des deux projets.

### Exemple 3:

Veuillez entrer la liste des professeurs de projet 1: Francois Jean Martin Stephane Alexandre Joseph
Veuillez entrer la liste des professeurs de projet 2: Francois Jean Martin Stephane Alexandre Maxime
Joseph et Maxime sont les professeurs qui enseignent un seul des deux projets.

### Exemple 4:

Veuillez entrer la liste des professeurs de projet 1: Francois Jean Martin Stephane Alexandre Joseph
Veuillez entrer la liste des professeurs de projet 2: Francois Jean Martin Stephane Alexandre Joseph
Il n'y a pas de professeurs qui enseignent un seul des deux projets.

### Exemple 5:
Veuillez entrer la liste des professeurs de projet 1: Stephane Martin Camille stephane
Veuillez entrer la liste des professeurs de projet 2: Martin camille  
Les professeurs suivants enseignent un seul des deux projets: ['Camille', 'Stephane', 'camille', 'stephane']

"""

# TODO: Commencez votre programme ici

professeurs1 = set(input("Veuillez entrer la liste des professeurs de projet 1: ").split())
professeurs2 = set(input("Veuillez entrer la liste des professeurs de projet 2: ").split())

difference = list(professeurs1.symmetric_difference(professeurs2))
difference.sort()

if len(difference) == 0:
    print("Il n'y a pas de professeurs qui enseignent un seul des deux projets.")
elif len(difference) == 1:
    print(f"{difference[0]} est le seul professeur qui enseigne un seul des deux projets.")
elif len(difference) == 2:
    print(f"{difference[0]} et {difference[1]} sont les professeurs qui enseignent un seul des deux projets.")
else:
    print(f"Les professeurs suivants enseignent un seul des deux projets: {difference}")



