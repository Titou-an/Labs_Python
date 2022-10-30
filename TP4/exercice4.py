"""
exercice4.py
Description : Trier les etudiants
Auteurs     : William Morin (2213763), Théo Manach (2058412)
"""

"""
Vous devez écrire un programme permettant de trier les étudiants en fonction de leur résultat à l'examen de mi-session.

Votre programme débute en demandant combien d'étudiants il faut trier.
Vous devez vous assurer que l'utilisateur indique un nombre entier strictement positif (c'est-à-dire > 0).

Par la suite, pour chaque étudiant, votre programme doit demander le prenom suivi de son résultat à l'examen de mi-session.
Vous devez vous assurer que le résultat est un nombre entier dans l'intervalle [0, 20] 

Par la suite, vous devez afficher chaque étudiant comme un tuple (Prenom, Note) dans l'ordre croissant de note.
* Indice: la fonction sorted(..., key=lambda x: ...) pourrait être utile ici.

### Exemple 1
Veuillez entrer le nombre d'étudiants: -1
Veuillez entrer le nombre d'étudiants: 0
Veuillez entrer le nombre d'étudiants: 2
Veuillez entrer son prénom: Marcel
Veuillez entrer sa note: 17
Veuillez entrer son prénom: Gino
Veuillez entrer sa note: 22
Veuillez entrer sa note: 20
('Marcel', 17)
('Gino', 20)

### Exemple 2
Veuillez entrer le nombre d'étudiants: 3
Veuillez entrer son prénom: Marcel
Veuillez entrer sa note: 22
Veuillez entrer sa note: -1
Veuillez entrer sa note: 15
Veuillez entrer son prénom: Camille
Veuillez entrer sa note: 14
Veuillez entrer son prénom: Élodie
Veuillez entrer sa note: 19
('Camille', 14)
('Marcel', 15)
('Élodie', 19)
"""

# TODO: Commencez votre programme ici

while True:
    nbr_etudiant = input("Veuillez entrer le nombre d'étudiants: ")
    if nbr_etudiant.isdigit():
        nbr_etudiant = int(nbr_etudiant)
        if nbr_etudiant > 0:
            break

resultats = []

for etudiant in range(nbr_etudiant):
    nom = input("Veuillez entrer son prénom: ")

    while True:
        note = input("Veuillez entrer sa note: ")
        if note.isdigit():
            note = int(note)
            if note in range(0, 21):
                break

    resultats.append(tuple((nom, note)))

resultats.sort(key=lambda x: x[1])

for res in resultats:
    print(res)
