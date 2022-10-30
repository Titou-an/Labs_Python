"""
exercice1.py
Description : Pangramme
Auteurs     : William Morin (2213763), Théo Manach (2058412)
"""

"""
Vous devez concevoir un programme permettant de tester des claviers d'ordinateurs.
Pour ce faire, votre programme doit vérifier si une phrase est un pangramme (https://fr.wikipedia.org/wiki/Pangramme)
En testant les claviers avec des pangrammes, on s'assure que toutes les touches sont fonctionnelles :)

Votre programme doit commencer par demander une phrase à l'utilisateur.
Ensuite, il doit afficher, en ordre alphabétique, les lettres manquantes dans la phrase pour que celle-ci soit un pangramme.
Finalement, votre programme doit afficher dans quels mots on retrouve chaque lettre de l'alphabet. Pour ce faire, vous devez afficher
un dictionnaire qui contient, pour chaque lettre, une liste en ordre alphabétique qui contient chaque mot ayant cette lettre.

Pour determiner les mots dans la phrase, vous pouvez considerer que chaque mot est separé par un espace.
Vous pouvez vous servir de la variable alphabet qui est une chaine de caractères contenant toute les lettres de l'alphabet en minuscule, en ordre alphabétique.

Il n'est pas nécessaire de retirer les caractères non-alphabétiques (p. ex.: ,#$%& etc...)

### Exemple #1:
Veuillez indiquer votre phrase: Monsieur Jack, vous dactylographiez bien mieux que Wolf
[]
{'a': ['dactylographiez', 'jack,'], 'b': ['bien'], 'c': ['dactylographiez', 'jack,'], 'd': ['dactylographiez'], 'e': ['bien', 'dactylographiez', 'mieux', 'monsieur', 'que'], 'f': ['wolf'], 'g': ['dactylographiez'], 'h': ['dactylographiez'], 'i': ['bien', 'dactylographiez', 'mieux', 'monsieur'], 'j': ['jack,'], 'k': ['jack,'], 'l': ['dactylographiez', 'wolf'], 
'm': ['mieux', 'monsieur'], 'n': ['bien', 'monsieur'], 'o': ['dactylographiez', 'monsieur', 'vous', 'wolf'], 'p': ['dactylographiez'], 'q': ['que'], 'r': ['dactylographiez', 'monsieur'], 's': ['monsieur', 'vous'], 't': ['dactylographiez'], 'u': ['mieux', 'monsieur', 'que', 'vous'], 'v': ['vous'], 'w': ['wolf'], 'x': ['mieux'], 'y': ['dactylographiez'], 'z': ['dactylographiez']}

### Exemple #2:
Veuillez indiquer votre phrase: monsieur jack, vous dactylographiez bien mieux que wolf
[]
{'a': ['dactylographiez', 'jack,'], 'b': ['bien'], 'c': ['dactylographiez', 'jack,'], 'd': ['dactylographiez'], 'e': ['bien', 'dactylographiez', 'mieux', 'monsieur', 'que'], 'f': ['wolf'], 'g': ['dactylographiez'], 'h': ['dactylographiez'], 'i': ['bien', 'dactylographiez', 'mieux', 'monsieur'], 'j': ['jack,'], 'k': ['jack,'], 'l': ['dactylographiez', 'wolf'], 
'm': ['mieux', 'monsieur'], 'n': ['bien', 'monsieur'], 'o': ['dactylographiez', 'monsieur', 'vous', 'wolf'], 'p': ['dactylographiez'], 'q': ['que'], 'r': ['dactylographiez', 'monsieur'], 's': ['monsieur', 'vous'], 't': ['dactylographiez'], 'u': ['mieux', 'monsieur', 'que', 'vous'], 'v': ['vous'], 'w': ['wolf'], 'x': ['mieux'], 'y': ['dactylographiez'], 'z': ['dactylographiez']}


### Exemple #3:
Veuillez indiquer votre phrase: Monsieur Jack, vous dactylographiez bien mieux que olf
['w']
{'a': ['dactylographiez', 'jack,'], 'b': ['bien'], 'c': ['dactylographiez', 'jack,'], 'd': ['dactylographiez'], 'e': ['bien', 'dactylographiez', 'mieux', 'monsieur', 'que'], 'f': ['olf'], 'g': ['dactylographiez'], 'h': ['dactylographiez'], 'i': ['bien', 'dactylographiez', 'mieux', 'monsieur'], 'j': ['jack,'], 'k': ['jack,'], 'l': ['dactylographiez', 'olf'], 'm': ['mieux', 'monsieur'], 'n': ['bien', 'monsieur'], 'o': ['dactylographiez', 'monsieur', 'olf', 'vous'], 'p': ['dactylographiez'], 'q': ['que'], 'r': ['dactylographiez', 'monsieur'], 's': ['monsieur', 'vous'], 't': ['dactylographiez'], 'u': ['mieux', 'monsieur', 'que', 'vous'], 'v': ['vous'], 'w': [], 'x': ['mieux'], 'y': ['dactylographiez'], 'z': ['dactylographiez']}

### Example #4:
Veuillez indiquer votre phrase: salut
['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 'v', 'w', 'x', 'y', 'z']
{'a': ['salut'], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': ['salut'], 'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': ['salut'], 't': ['salut'], 'u': ['salut'], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}
"""

import string

alphabet = string.ascii_lowercase
# TODO: Commencez votre programme ici

phrase = input("Veuillez indiquer votre phrase: ")
manquants = []
dict = {}

for lettre in alphabet:
    dict[lettre] = []
    if lettre not in phrase.casefold():
        manquants.append(lettre)

mots = phrase.split()

for mot in mots:
    for lettre in alphabet:
        if lettre in mot.casefold():
            dict[lettre].append(mot.casefold())
        dict[lettre].sort()

print(manquants)
print(dict)
