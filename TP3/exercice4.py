__version__ = "TP3 - Exercice #4"
__author__ = "William Morin (2213763), Théo Manach (2058412)"

"""
La compagnie Coca-cola a décidé en 2022 de mettre en place une politique pour favoriser le
recyclage des contenants plastiques : "Une bouteille de Coca-Cola pour 'm' bouteilles vides
retournées".
Votre petit frère, amoureux de cette boisson vous demande de lui écrire un programme qui
prend en entrée :
- Le nombre de bouteilles vides initialement (dans l'exemple 2 ce nombre vaut 1). Ce nombre
doit être un entier positif.
- Le nombre de bouteilles pleines initiales que son budget lui permet d'acheter (dans l'exemple
2 ce nombre vaut 8). Ce nombre doit être un entier positif.
- Le nombre de bouteilles échangeables 'm' (dans l'exemple 2 ce nombre vaut 3). Ce nombre doit
être un entier supérieur ou égal à 2.
Le programme devrait afficher en sortie le nombre de bouteilles qui pourront être consommées
à la fin du processus ainsi que le nombre de bouteilles vides restantes. La validation
d'entrée n'est pas demandée.
Remarque : Ce problème est resolvable analytiquement en utilisant les suites géométriques.
Cependant, on vous demande de ne pas implémenter cette solution. On s'attend à une solution
itérative utilisant au moins une boucle.
========================================= Exemple 1 =========================================
$ python3 exercice4.py
Veuillez entrer le nombre de bouteilles vides : 0
Veuillez entrer le nombre de bouteilles pleines : 8
Veuillez entrer le nombre de bouteilles vides echangeables : 3
Vous pouvez boire exactement 11 bouteille(s)
Il vous restera 2 bouteille(s) vide(s) a la fin
========================================= Exemple 2 =========================================
$ python3 exercice4.py
Veuillez entrer le nombre de bouteilles vides : 1
Veuillez entrer le nombre de bouteilles pleines : 8
Veuillez entrer le nombre de bouteilles vides echangeables : 3
Vous pouvez boire exactement 12 bouteille(s)
Il vous restera 1 bouteille(s) vide(s) a la fin
"""

# TODO : Ajouter votre code

bVide = int(input("Veuillez entrer le nombre de bouteilles vides :"))
bPleine = int(input("Veuillez entrer le nombre de bouteilles pleines :"))
bEchange = int(input("Veuillez entrer le nombre de bouteilles vides echangeables :"))

compteur = bPleine

while (bVide+bPleine) >= bEchange:
    bVide += bPleine
    
    bPleine = bVide // bEchange
    bVide = bVide % bEchange

    compteur += bPleine


print("Vous pouvez boire exactement", compteur, "bouteille(s)")
print("Il vous restera", bVide+bPleine, "bouteille(s) vide(s) a la fin")
