__version__ = "TP5 - Exercice #1"
__author__ = " William Morin (2213763), Théo Manach (2058412)"

import keyword

from taste_the_rainbow import *
import string
import random

codeMort = ['//[0x7f]', '//[0x00]', '//[0x07]', '//[0x1e]', "_ZN4ctrl1vC1Ev", "_ZN4util1jC1Ev", "_ZN3doc1bC1Ev",
            "_ZN4cond1mC1Ev", "_ZN4spec1qC1Ev"]

"""
 * <PARTIE 1.1 DU MANDAT>
 * Retourne le contenu d'un fichier.
 * @param chemin_fichier    (str) Le chemin vers le fichier.
 * @return                  (str) Le contenu du fichier.
"""


def charger_contenu(chemin_fichier):
    contenu = ""
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        contenu = f.read()

    return contenu


"""
 * <PARTIE 1.2 DU MANDAT>
 * Crée un dictionnaire qui devrait lier le code obfusqué lu en tant que clé au code équivalent en Python (valeur).
 * Attention! Cette fonction devrait faire usage des fonctions hex(), ord() ou chr() et non bêtement copier la table
 * présentée au Tableau 1. La moitié des points sera justement accordée pour l'ingéniosité de votre
 * implémentation (pensez à user des imports et à regarder dans la documentation pour des fonctions simples qui font
 * une partie du travail à votre place !).
 * @return (dict) Un tel dictionnaire.
"""


def creer_dictionnaire():
    dictionnaire = {
    }

    # Dictionnaire des mots clés et de leur lettre correspondante
    lettreMotCle = {
        "4ctrl1": {  # Control
            "i": "if",
            "e": "else",
            "w": "while",
            "f": "for",
            "r": "range",
            "t": "try",
            "x": "except",
            "v": ""  # code mort
        },
        "4util1": {  # Utility
            "i": "import",
            "f": "from",
            "j": ""  # code mort
        },
        "3doc1": {  # Documentation
            "t": "__title__",
            "a": "__author__",
            "c": "__copyright__",
            "b": ""  # code mort
        },
        "4cond1": {  # Conditional
            "n": "not",
            "a": "and",
            "s": "as",
            "m": ""  # code mort
        },
        "4spec1": {  # Special
            "p": "+=",
            "m": "-=",
            "q": ""  # code mort
        }
    }

    # Associe tous les mot cle à leur code obfusqué correspondant
    for cat in lettreMotCle.keys():
        for ltr in lettreMotCle[cat].keys():
            dictionnaire["_ZN" + cat + ltr + "C1Ev"] = lettreMotCle[cat][ltr]

    # Associe tous les characteres imprimables à leur code obfusqué correspondant
    for char in ((set(string.ascii_letters).union(string.digits)).union(
            {" ", "\n", "(", ")", "*", "[", "]", "{", "}", "#", ".", "\"", "\'", "/", "=", ";", ":", "<", ">", "_", "-",
             "\\", "+", ","})):
        valHex = "0x%02x" % (ord(char))
        dictionnaire["//[" + valHex + "]"] = char

    for code_mort in codeMort:
        dictionnaire[code_mort] = ""

    return dictionnaire


"""
 * <PARTIE 1.3 DU MANDAT>
 * À partir de votre dictionnaire nouvellement créé, transpilez le contenu du programme-brumeux.txt au sein 
 * du fichier programme-decouvert.txt. Il faut transpiler le contenu du fichier au chemin 'chemin_fichier_brumeux',
 * et l'écrire dans le fichier au chemin 'chemin_fichier_transpile'. Si ce fichier n'existe pas déjà, il doit être créé. Pareillement, 
 * s'il existe déjà, son contenu doit être écrasé à chaque fois que ce script est exécuté.
 * Attention! Votre code doit utiliser les chemins de fichiers donnés en paramètre de cette fonction.
 * Attention! Votre code doit utiliser vos fonctions 'charger_contenu' et 'creer_dictionnaire'!
 * @param chemin_fichier_brumeux    (str) Le chemin vers le fichier brumeux.
 * @param chemin_fichier_transpile  (str) Le chemin vers le fichier transpilé.
"""


def transpilation(chemin_fichier_brumeux, chemin_fichier_transpile):
    contenu = charger_contenu(chemin_fichier_brumeux)
    dict = creer_dictionnaire()

    for motObf, mot in dict.items():
        contenu = contenu.replace(motObf, mot)
    with open(chemin_fichier_transpile, 'w', encoding="utf-8") as f:
        f.write(contenu)


"""
 * <PARTIE 2.0 DU MANDAT>
 * Cette fonction permet d'ajouter du code mort aléatoire à votre programme à découvert 50% du temps.
 * Pour la partie aléatoire, vous devez l'implémenter en utilisant la fonction random() ou randint() de la librairie random.
 * Votre programme devrait donc retourner soit None, soit du code mort aléatoire en string (les deux d'une possibilité de 50%).
 * N'oubliez pas de vérifier le paramètre de la fonction (à savoir si les choix de possibilités de code mort ne correspondent pas à 
 * un tableau vide, par exemple) ! La chaîne de caractères retournée doit être choisie de manière aléatoire parmi les possibilités
 * de code mort (possibilites_code_mort). Vous pouvez faire usage, par exemple, de la fonction random.choice(...) pour arriver à vos
 * fins.
 * @param possibilites_code_mort (list) Liste des possibilités de code mort à ajouter le cas échéant.
 * @return None ou string (représentant le code mort).
"""


def generer_code_mort(possibilites_code_mort):
    if len(possibilites_code_mort) != 0:
        if random.randint(0, 1) == 0:
            return random.choice(possibilites_code_mort)

    return None


"""
 * <PARTIE 2.1 DU MANDAT>
 * À partir du contenu du programme à découvert venant du fichier programme-a-obfusquer.txt, veuillez obfusquer son contenu 
 * dans un second fichier, nommé programme-obfusque.txt. Si ce fichier n'existe pas déjà, il doit être créé. 
 * Pareillement, s'il existe déjà, son contenu doit être écrasé à chaque fois que ce script est exécuté.
 * Vous devez vous servir des fonctions réalisées précédemment pour parvenir à vos fins. 
 * Ici, vous devez vérifier si la partie lue correspond à une structure de contrôle en premier et vérifier dans votre 
 * dictionnaire sa concordance en assembleur. Un tiers des points est accordé au respect de cette préséance.
 * Chaque fois que vous ajoutez du contenu obfusqué, vous devriez vérifier s'il faut aussi ajouter du code mort.
 * Un tiers des points est accordé à une utilisation judicieuse de la fonction generer_code_mort() au sein de votre fonction
 * d'obfuscation. Vous devriez vérifier s'il faut ajouter du code mort à chaque insertion d'un caractère ou d'une structure
 * de contrôle. Indice: les espaces sont aussi des caractères !
 * @param chemin_fichier_a_obfusquer    (str) Le chemin vers le fichier a obfusquer.
 * @param chemin_fichier_obfusque       (str) Le chemin vers le fichier obfusqué.
"""


def obfuscation(chemin_fichier_a_obfusquer, chemin_fichier_obfusque):
    contenu = charger_contenu(chemin_fichier_a_obfusquer)
    contenu_fichier = ""

    dict = creer_dictionnaire()

    for ligne in contenu.splitlines(True):
        for mot in ligne.split(" "):
            if mot in dict.values():
                cm = generer_code_mort(codeMort)
                contenu_fichier += list(dict.keys())[list(dict.values()).index(mot)] + ("" if cm == None else cm)
            else:
                for char in mot:
                    cm = generer_code_mort(codeMort)
                    contenu_fichier += list(dict.keys())[list(dict.values()).index(char)] + ("" if cm == None else cm)

            if not mot.endswith("\n"):
                cm = generer_code_mort(codeMort)
                contenu_fichier += list(dict.keys())[list(dict.values()).index(" ")] + ("" if cm == None else cm)

    with open(chemin_fichier_obfusque, 'w', encoding="utf-8") as f:
        f.write(contenu_fichier)


if __name__ == "__main__":
    # Ne pas toucher à la section ci-bas
    CATEGORY = "EXERCICE_1"
    try:
        print_header(CATEGORY, "-- Partie 1 du mandat --")
        print_header(CATEGORY, 'Transpilation du fichier programme-brumeux.txt vers programme-decouvert.txt...')
        transpilation("programme-brumeux.txt", "programme-decouvert.txt")
        print_success(CATEGORY, "Transpilation terminee !")
        print('')
        print_header(CATEGORY, "-- Partie 2 du mandat --")
        print_header(CATEGORY, 'Obfuscation du fichier programme-a-obfusquer.txt vers programme-obfusque.txt...')
        obfuscation("programme-a-obfusquer.txt", "programme-obfusque.txt")
        print_success(CATEGORY, "Obfuscation terminee !")
    except Exception as e:
        print_warning(CATEGORY, "Erreur fatale survenue lors de l'execution de votre exercice 1.")
        print_failure(CATEGORY, e.__str__())
    # Ne pas toucher à la section ci-haut
