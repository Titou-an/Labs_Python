"""
exercice7.py
Description : Anagrammes
Auteurs     : William Morin (2213763), Théo Manach (2058412)
"""

"""
Écrire un programme qui demande à l'utilisateur d'entrer deux mots. 
Évaluer ensuite si ces deux mots sont des anagrammes.

Un anagramme est mot formé en changeant de place les lettres d'un autre mot.
Par exemple ARBRE et BARRE sont des anagrammes.

S'ils le sont, affichez "Les deux mots sont des anagrammes".
Sinon, affichez "Les deux mots ne sont pas des anagrammes".

* Important : Utiliser les methodes sort() ou sorted() est INTERDIT. 0 points seront attribués
si elles sont utilisées.
* Indice : Utiliser un ou des dictionnaire(s).

### Exemple 1 
Entrer le premier mot: manger
Entrer le deuxieme mot: partir
Les deux mots ne sont pas des anagrammes

### Exemple 2 
Entrer le premier mot: migraine
Entrer le deuxieme mot: imaginer
Les deux mots sont des anagrammes

"""

# TODO: Commencez votre programme ici

mot1 = input("Entrer le premier mot: ")
mot2 = input("Entrer le deuxieme mot: ")
anagramme = True

for lettre in mot1:
    if mot1.count(lettre) != mot2.count(lettre):
        anagramme = False

if anagramme:
    print("Les deux mots sont des anagrammes")
else:
    print("Les deux mots ne sont pas des anagrammes")