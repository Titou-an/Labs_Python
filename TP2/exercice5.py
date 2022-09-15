__version__ = "TP2 - Exercice #5"
__author__ = "William Morin (2213763), Théo Manach (2058412)"

# Écrire un programme qui calcule la montant d'argent à payer par personne d'un groupe d'ami(e)s
# dans un restaurant, après avoir choisi le pourcentage de pourboire (tips) 
# et le nombre de membres du groupe.
# Voir exemples ci-dessous.

# Tous les prix affichés doivent être arrondis à deux chiffres après la virgule.

"""

#### Exemple d'éxécution #1
---- Calculateur de pourboire ----
Quel est le montant de la facture initiale? 22.65
Quel est le pourcentage de pourboire? 10, 12, ou 15? 10
Combien de personnes y a-t-il dans le groupe? 2
Pourboire total: $ 2.27
Pourboire par membre: $ 1.13
--- Coût total ---
Facture totale: $ 24.91
Chacun doit payer: $ 12.46


#### Exemple d'éxécution #2

---- Calculateur de pourboire ----
Quel est le montant de la facture initiale? 274.25
Quel est le pourcentage de pourboire? 10, 12, ou 15? 12
Combien de personnes y a-t-il dans le groupe? 9
Pourboire total: $ 32.91
Pourboire par membre: $ 3.66
--- Coût total ---
Facture totale: $ 307.16
Chacun doit payer: $ 34.13

"""
# TODO: Commencez votre programme ici

print("---- Calculateur de pourboire ----")
montant = float(input("Quel est le montant de la facture initiale?"))
pourcentage = int(input("Quel est le pourcentage de pourboire? 10, 12, ou 15?")) / 100
personnes = int(input("Combien de personnes y a-t-il dans le groupe?"))

pourboire = montant * pourcentage
total = pourboire + montant

print("Pourboire total: $", round(pourboire, 2))
print("Pourboire par membre: $", round(pourboire / personnes, 2))
print("--- Coût total ---")
print("Facture totale: $", round(total, 2))
print("Chacun doit payer: $", round(total / personnes, 2))
