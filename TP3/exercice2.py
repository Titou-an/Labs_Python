__version__ = "TP3 - Exercice #2"
__author__ = "William Morin (2213763), Théo Manach (2058412)"

"""
Le cryptage par chiffrement est un procédé en cryptographie
qui permet de rendre la compréhension d'un document impossible à toute personne qui
ne possède pas la clé de chiffrement. Autrement dit, c'est un moyen d'envoyer des
informations qu'on souhaite garder confidentielles à une personne désignée qui détient
la clé. La clé permet de traduire l'information afin qu'elle soit compréhensible pour le
destinataire.
Le code de César est une méthode de cryptage par décalage connue, jadis utilisée par
nul autre que Jules César. Si la clef de chiffrement est 3, alors on décale chaque
caractère de trois positions de l'alphabet le texte à encrypter. Attention la lettre X
correspond à A, Y à B et Z à C pour une clef de chiffrement de 3.

Attention, nous décalons uniquement les caractères alphabétiques.

Écrire un programme qui permet d'encrypter un texte avec le code de César en connaissant
la clé.
========================================== Exemple ==========================================
$ python3 exercice2.py
Veuillez entrer un texte : Allo, poly
Veuillez entrer la cle de chiffrement : 3
Votre texte chiffre est : "Door, srob"
"""

# TODO : Ajouter votre code
msg = input("Veuillez entrer un texte :")
cle = int(input("Veuillez entrer la cle de chiffrement :"))

resultat = ""
for lettre in msg:
    if lettre.isalpha():
        pos = ord(lettre)
        if lettre.isupper():
            resultat += chr((pos - 65 + cle) % 26 + 65)
        else:
            resultat += chr((pos - 97 + cle) % 26 + 97)
    else:
        resultat += lettre

print("Votre texte chiffre est :", "\"" + resultat + "\"")
