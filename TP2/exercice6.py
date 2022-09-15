__version__ =   "TP2 - Exercice #6"
__author__  =   "William Morin (2213763), Théo Manach (2058412)"

import math

# Vous devez écrire un programme qui permet d'éffectuer les opérations de somme,
# de produit, calcul de module, de test et de conversion sur deux nombres complexes entrés par l'utilisateur.
# Voir exemples ci-dessous.

# Vous devez arrondir le module du produit à 2 décimales.

# Indice: pour savoir si un nombre complexe est un réel pur un imaginaire pur, utilisez la méthode suivante:
#     nombre_complexe.real == 0 ou nombre_complex.imag == 0

"""
#### Exemple d'éxécution #1

Veuillez entrer le premier nombre complexe: 1+j
Veuillez entrer le deuxième nombre complexe: 1+j
La somme est de: (2+2j)
La somme est un réel pur : False
Le produit est de: 2j
Le produit est un imaginaire pur : True
Le module du produit est de : 2.0
La partie entière du module du produit en binaire est de : 0b10
La partie entière du module du produit en hexadécimal est de : 0x2


#### Exemple d'éxécution #2

Veuillez entrer le premier nombre complexe: -12+j
Veuillez entrer le deuxième nombre complexe: 21-j
La somme est de: (9+0j)
La somme est un réel pur: True
Le produit est de: (-251+33j)
Le produit est un imaginaire pur: False
Le module du produit est de: 253.16
La partie entière du module du produit en binaire est de: 0b11111101
La partie entière du module du produit en hexadécimal est de: 0xfd
"""

# TODO: Commencez votre programme ici

c1 = complex(input("Veuillez entrer le premier nombre complexe: "))
c2 = complex(input("Veuillez entrer le deuxième nombre complexe: "))

somme = c1 + c2
produit = c1 * c2
module = math.sqrt(produit.real**2+produit.imag**2)

print("La somme est de:", somme)
print("La somme est un réel pur:", somme.imag == 0)
print("Le produit est de:", produit)
print("Le produit est un imaginaire pur:", produit.real == 0)
print("Le module du produit est de:", round(module,2))
print("La partie entière du module du produit en binaire est de:", bin(int(module.real)))
print("La partie entière du module du produit en hexadecimal est de:", hex(int(module.real)))