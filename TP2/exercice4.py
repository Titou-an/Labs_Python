__version__ =   "TP2 - Exercice #4"
__author__  =   "William Morin (2213763), Théo Manach (2058412)"

# Écrire un programme qui permet d'évaluer le nombre d'heures d'étude d'un cours 
# à partir du nombre de jours d'étude et du nombre d'heures d'étude par jours.
# Vous devez également dire si le budget d'études (50 heures) sera dépassé ou non.

# Considérez que le nombre de séances est un nombre entier et que
# le nombre d'heures d'étude par séance est un nombre décimal.

"""
#### Exemple d'éxécution #1
----- Planificateur d'étude -----
Bonjour, veuillez entrer le nom du cours: Introduction à Python
Veuillez entrer le nombre de séances d'étude: 21
Veuillez entrer le nombre d'heure(s) d'étude par séance: 1.5
Le cours Introduction à Python
A besoin d'un nombre d'heures d'étude de : 31.5 heure(s)
Le budget d'étude est dépassé: False
----- Fin de programme, merci et à très bientôt -----

#### Exemple d'éxécution #2

----- Planificateur d'étude -----
Bonjour, veuillez entrer le nom du cours: Algèbre linéaire
Veuillez entrer le nombre de séances d'étude: 28
Veuillez entrer le nombre d'heure(s) d'étude par séance: 2
Le cours Algèbre linéaire
A besoin d'un nombre d'heures d'étude de : 56.0 heure(s)
Le budget d'étude est dépassé: True
----- Fin de programme, merci et à très bientôt -----
"""

# TODO: Commencez votre programme ici

print("----- Planificateur d'étude -----")

cours = input("Bonjour, veuillez entrer le nom du cours:")
seances = int(input("Veuillez entrer le nombre de séances d'étude:"))
heures = float(input("Veuillez entrer le nombre d'heure(s) d'étude par séance:"))

print("Le cours", cours)
print("A besoin d'un nombre d'heures d'étude de :", seances * heures, "heure(s)")
print("Le budget d'étude est dépassé:", (seances * heures) > 50)
print("----- Fin de programme, merci et à très bientôt -----")