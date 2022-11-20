__version__ = "TP5 - Exercice #2"
__author__ = " William Morin (2213763), Théo Manach (2058412)"

import csv
import json
import os

# Vous pouvez utiliser ces constantes dans votre code.
delimiteur_csv = ','
chemin_fichier_rapport_json = 'rapport.json'
indentation_json = 4
chemin_fichiers_temperature = '//data-exercice2//'
precision_arrondissement = 2

"""
 * Retourne le répertoire courant.
 * @return (str) Le répertoire courant.
"""


def get_repertoire_courant():
    return os.getcwd()


"""
 * Retourne les noms des fichiers de température.
 * @return (list[str]) Les noms des fichiers de température.
"""


def get_noms_fichiers_temperature():
    return os.listdir(get_repertoire_courant() + chemin_fichiers_temperature)


"""
 * <PARTIE 1.1 DU MANDAT>
 * Créez un dictionnaire des températures des régions et territoires. Les clefs de votre dictionnaire sont des pays.
 * Lorsque vous accédez au contenu de votre dictionnaire principal, cela vous retourne un second dictionnaire contenant toutes 
 * les régions liées au pays.
 * Votre fonction devrait faire usage des fonctions get_repertoire_courant() et get_noms_fichiers_temperature() déjà écrites
 * pour vous ci-haut pour parcourir les températures enregistrées des 229 pays.
 * Attention : vous ne pouvez pas bêtement prendre la température annuelle (« Annual ») qui figure au sein de vos fichiers .csv,
 * étant trop arrondie. Vous devez faire la moyenne des températures enregistrées de janvier à décembre pour lesdites régions avant 
 * de l'enregistrer au sein de votre dictionnaire.
 * @return (dict[dict[float]]) Un dictionnaire de pays contenant des dictionnaires de régions listant leurs températures.
"""


def creer_dictionnaire_temp_regions():
    dictionnaire = {}

    for file in get_noms_fichiers_temperature():
        with open(get_repertoire_courant() + chemin_fichiers_temperature + file, encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=delimiteur_csv)

            # Saute les deux premieres rangees
            next(reader)
            next(reader)

            pays = next(reader)[0]
            regions = {}

            # Creation de dictionnaires contennant les regions et leurs temperatures
            for row in reader:
                moyenne = 0.0

                # Fait la moyenne des temperatures de la region
                for temp in row[2:]:
                    moyenne += float(temp)

                moyenne /= len(row[2:])

                regions[row[0]] = moyenne

            dictionnaire[pays] = regions

    return dictionnaire


"""
 * <PARTIE 1.2 DU MANDAT>
 * Créez un dictionnaire des températures des pays à partir de votre dictionnaire créé à la partie 1.1 du mandat. Pour ce faire,
 * vous devez parcourir toutes les températures des régions associées à un pays et faire une moyenne de leurs températures qui 
 * correspondra, en vain, à la température moyenne du pays. Vous devriez faire usage de la fonction creer_dictionnaire_temp_regions().
 * Évidemment, il y a des pays sans région ni territoire. Un tel pays aura donc une température moyenne de 0.
 * Vos températures finales devraient être arrondies à 2 unités après la virgule.
 * @return (dict[float]) Un dictionnaire de pays contenant leurs températures moyennes arrondies à 2 unités après la virgule.
"""


def creer_dictionnaire_temp_pays():
    dictRegion = creer_dictionnaire_temp_regions()
    dictionnaire = {}

    for pays in dictRegion.keys():
        moyenne = 0.0

        if len(dictRegion[pays]) != 0:
            for temp in dictRegion[pays].values():
                moyenne += temp

            moyenne /= len(dictRegion[pays])

        dictionnaire[pays] = round(moyenne, 2)

    return dictionnaire


"""
 * <PARTIE 1.3 DU MANDAT>
 * À partir de votre dictionnaire des températures créé à la partie 1.2 de votre mandat, trouvez les 5 pays les plus chauds / torrides.
 * Vous devriez avoir une liste de 5 tuples, dont le membre de gauche du tuple correspond au pays (str) et le membre de droite à la température
 * moyenne du pays (float), arrondie à 2 unités après la virgule. Vous devriez utiliser la fonction creer_dictionnaire_temp_pays().
 * Indice: la fonction sorted(..., key=lambda x: ...) serait particulièrement utile ici...
 * @return (list[tuple[str, float]]) Une liste de 5 tuples dont le premier membre du tuple correspond au pays et, le second, à sa température.
"""


def cinq_pays_les_plus_torrides():
    top5 = []
    dict = creer_dictionnaire_temp_pays()

    # Trie la liste des pays
    liste = sorted(dict, key=lambda x: dict[x], reverse=True)

    for i in range(5):
        top5.append((liste[i], dict[liste[i]]))

    return top5


"""
 * <PARTIE 1.4 DU MANDAT>
 * Faites un rapport en format .json, nommé rapport.json, dont figurent les 5 pays les plus torrides.
"""

def generer_rapport_pays_torrides():
    top5 = dict(cinq_pays_les_plus_torrides())
    with open(chemin_fichier_rapport_json, "w") as f:
        json.dump(top5, f)
