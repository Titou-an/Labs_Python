__version__ = "TP2 - Exercice #2"
__author__ = "William Morin (2213763), Théo Manach (2058412)"

import datetime

# Vous devez écrire un programme qui formatte la date de naissance d'un utilisateur.
# Vous devez commencer par demander le jour, le mois et l'année de naissance de l'utilisateur.
# Ensuite, vous devez afficher sa date de naissance selon le format jour-mois-année.
# Votre programme doit aussi calculer l'âge que l'utilisateur aura à la fin de l'année 2022.
# Voir exemples ci-dessous.

"""
Exemple 1:
Veuillez entrer le jour : 12
Veuillez entrer le mois : 4
Veuillez entrer l'année : 2000
L'utilisateur est né le 12-4-2000 et il aura 22 ans à la fin de l'année.

Exemple 2:
Veuillez entrer le jour : 25
Veuillez entrer le mois : 12
Veuillez entrer l'année : 1950
L'utilisateur est né le 25-12-1950 et il aura 72 ans à la fin de l'année.
"""

# TODO: Commencez votre programme ici

jour = int(input("Veuillez entrer le jour :"))
mois = int(input("Veuillez entrer le mois :"))
annee = int(input("Veuillez entrer l'année :"))

date = datetime.date(annee, mois, jour)

print(
    "L'utilisateur est né le", date.strftime("%d-%m-%Y"),
    "et il aura", datetime.date.today().year - date.year, "ans à la fin de l'année.")
