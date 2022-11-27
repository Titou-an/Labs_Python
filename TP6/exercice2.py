"""
exercice2.py
Exercice 2 du TP6 du cours INF1005D
Description : Programme qui permet d'analyser les données des incidents du métro de Montréal.
Auteurs     : William Morin (2213763), Théo Manach (2058412)
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')


def incidents_par_ligne():
    """
    Permet de comptabiliser le nombre d'incidents par ligne de métro à partir du fichier CSV d'incidents.
    Ces données proviennent de https://donnees.montreal.ca/societe-de-transport-de-montreal/incidents-du-reseau-du-metro, 
    mais ont été légèrement modifiées par l'équipe du cours INF1005D pour simplifier votre code.

    Vous devez appliquer les filtres suivants:
    1. On s'intéresse uniquement aux incidents de l'année 2019.
    2. On s'intéresse uniquement aux incidents de type "T" (pour train, et non "S" pour station). Il s'agit de la 2e colonne: type_incident.
    3. On s'intéresse uniquement aux incidents d'au moins 5 minutes (>=), ce qui est la norme internationale pour comparer les réseaux de métro.

    Paramètres de la fonction :
        Aucun.

    Valeur de retour :
        Un dictionnaire contenant le nombre d'incidents par ligne de métro. Votre dictionnaire doit donc avoir quatre cléfs, soit:
        'orange', 'verte', 'jaune' et 'bleue' et le nombre d'incidents sur chacune de ces lignes comme valeurs.
    """

    # Retirez "pass" et écrivez votre code ici

    nombre_incidents = {"orange": 0,
                        "verte": 0,
                        "jaune": 0,
                        "bleue": 0}

    with open("incidents_metro.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for incident in reader:
            if int(incident[7]) == 2019:
                if incident[1] == "T":
                    if int(incident[11]) >= 5:
                        nombre_incidents["orange"] += int(incident[3])
                        nombre_incidents["verte"] += int(incident[4])
                        nombre_incidents["jaune"] += int(incident[5])
                        nombre_incidents["bleue"] += int(incident[6])

    return nombre_incidents


def incidents_par_mois():
    """
    Permet de comptabiliser le nombre d'incidents par mois à partir du fichier CSV d'incidents.
    Ces données proviennent de https://donnees.montreal.ca/societe-de-transport-de-montreal/incidents-du-reseau-du-metro, 
    mais ont été légèrement modifiées par l'équipe du cours INF1005D pour simplifier votre code.

    Vous devez appliquer les filtres suivants:
    1. On s'intéresse uniquement aux incidents de l'année 2019.
    2. On s'intéresse uniquement aux incidents de type "T" (pour train, et non "S" pour station). Il s'agit de la 2e colonne: type_incident.
    3. On s'intéresse uniquement aux incidents d'au moins 5 minutes (>=), ce qui est la norme internationale pour comparer les réseaux de métro.
    
    Paramètres de la fonction :
        Aucun.

    Valeur de retour : une liste contenant 12 éléments, soit le nombre d'incidents pour chaque mois de l'année.
    """

    # Retirez "pass" et écrivez votre code ici

    nombre_incidents = list(np.zeros(12, dtype=int))

    with open("incidents_metro.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for incident in reader:
            if int(incident[7]) == 2019:
                if incident[1] == "T":
                    if int(incident[11]) >= 5:
                        nombre_incidents[int(incident[8]) - 1] += 1

    return nombre_incidents


def graphique_incidents_par_ligne(incidents_data):
    """
    Permet d'afficher un graphique qui présente le nombre d'incidents par millions de km parcourus pour chaque ligne de métro.

    L'indicateur "incidents par millions de kilomètres parcourus" est une norme internationale pour comparer les réseaux de métro.
    Sans la division par le nombre de kilomètres parcourus, il est évident que les réseaux plus grands auront plus d'incidents, 
    ce qui n'est pas pertinent pour la comparaison.

    Cette fonction doit donc afficher un diagramme à bandes (voir énoncé PDF) qui montre
    le nombre d'incidents par millions de km parcourus pour chaque ligne de métro.

    En 2019, les trains du métro de Montréal ont parcourus le nombre suivant de kilomètres sur chaque ligne:
    Ligne verte :    32901843
    Ligne orange:    44430352
    Ligne jaune :     5035763
    Ligne bleue :     8526492
    Vous devrez utiliser ces valeurs lors du calcul. Pour vous aider, nous avons déjà créé une variable pour vous ("distance_parcourue_ligne").
    À noter que ces données proviennent de https://donnees.montreal.ca/societe-de-transport-de-montreal/stm-kilometrage-realise-par-les-voitures-de-metro-de-la-stm

    N'oubliez pas de diviser par 1 000 000 avant d'afficher votre graphique. On veut le nombre d'incidents par MILLION de kilomètres.

    Pour avoir tous vos points, votre graphique doit contenir les éléments suivants:
    1. Une grille en arrière plan. Indice: la fonction plt.grid(...)
    2. Des barres du diagramme de la bonne couleur pour chaque ligne (voir code ci-dessous)
    3. Le nombre d'incidents en haut de chaque barre (voir code ci-dessous)
    4. Des titres pour chaque axe
    5. Un titre en haut du graphique

    Paramètres de la fonction :
        Le dictionnaire créé par la fonction 'incidents_par_ligne'.

    Valeur de retour : rien.
    """

    # Retirez "pass" et écrivez votre code ici

    # Vous pouvez utiliser la variable suivante dans votre code
    distance_parcourue_ligne = {
        'verte': 32901843,
        'orange': 44430352,
        'jaune': 5035763,
        'bleue': 8526492
    }

    ### Utilisez la ligne suivante afin d'afficher les valeurs en haut des barres.
    ### La variable "bars" est la valeur retournée par la fonction "plt.bar(...)"
    ### Ainsi, votre code ci-dessus devrait ressembler à "bars = plt.bar(...)"
    # plt.gca().bar_label(bars, fmt='%.1f')

    ### Utilisez le code suivant pour mettre les bonne couleurs
    ### La variable "bars" est la valeur retournée par la fonction "plt.bar(...)"
    ### Attention! Votre diagramme doit avoir l'ordre : ligne verte, ligne orange, ligne jaune, ligne bleue
    # colors = ["#069037", "#F07D05", "#FAD706", "#057BC4"]
    # for color, bar in zip(colors, bars):
    #    bar.set_color(color)

    data_par_million = {}

    for ligne, nbr_incident in incidents_data.items():
        data_par_million[ligne] = (nbr_incident / distance_parcourue_ligne[ligne]) * 1000000

    fig, ax = plt.subplots()

    lignes = ["Ligne verte", "Ligne orange", "Ligne jaune", "Ligne bleue"]
    incidents = [data_par_million["verte"], data_par_million["orange"], data_par_million["jaune"],
                 data_par_million["bleue"]]
    colors = ["#069037", "#F07D05", "#FAD706", "#057BC4"]

    bars = ax.bar(lignes, incidents, color=colors)

    ax.set_title("Incidents par million de kilomètres \npour chaque ligne de métro en 2019")
    ax.set_ylabel("Arrêts de service par million de km")
    ax.set_xlabel("Ligne de métro")
    ax.bar_label(bars, fmt='%.1f')

    plt.grid(visible=True)
    plt.show()


def graphique_incidents_par_mois(incidents_data):
    """
    Permet d'afficher un graphique qui présente le nombre d'incidents (d'au moins 5 minutes) par mois en 2019 pour le métro de Montréal.

    Pour avoir tous vos points, votre graphique doit contenir les éléments suivants:
    1. Une grille en arrière plan. Indice: la fonction plt.grid(...)
    2. Les bons styles de lignes. 
       Indice: il s'agit des paramètres "color", "marker" et "linestyle" de la fonction plt.plot(...).
       Voir https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html pour les différentes options de linestyle.
       Voir https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers pour les différentes options de marker.
    3. Une ligne horizontale qui démontre le nombre moyen d'arrêts par mois.
       Indice: plt.axhline(y=..., color=..., linestyle=..., label=...)
    4. Un titre en haut du graphique
    5. Des titres pour les deux axes
    6. Une légende. Indice: la fonction plt.legend(...)
    7. Les mois de l'année sur l'axe horizontale. Indice: la fonction plt.xticks(...)

    Paramètres de la fonction :
        incidents_data: la liste créée par la fonction incidents_par_mois().
    Valeur de retour : rien.
    """

    # Retirez "pass" et écrivez votre code ici

    moyenne = 0

    for incident in incidents_data:
        moyenne += incident/12

    mois = ["Janv", "Févr", "Mars", "Avr", "Mai", "Juin", "Juill", "Août", "Sept", "Oct", "Nov", "Déc"]
    incidents = incidents_data

    fig, ax = plt.subplots()
    ax.plot(mois, incidents,color = "orange", ls = "--", marker = "o", label = "Nombre d'incidents par mois en 2019")
    ax.axhline(y =moyenne, color = "blue", ls=":",label = "Moyenne")

    ax.set_title("Nombre d'incidents par mois")
    ax.set_ylabel("Nombre d'incidents d'au moins 5 minutes")
    ax.set_xlabel("Mois")
    ax.legend()

    # plt.xticks(range(12),mois)
    plt.grid(visible=True)
    plt.show()


if __name__ == "__main__":
    # Ne modifiez pas cette section
    # Elle permet de tester vos fonctions :-)

    data_par_ligne = incidents_par_ligne()

    # Afficher le graphique des incidents par ligne
    graphique_incidents_par_ligne(data_par_ligne)

    data_par_mois = incidents_par_mois()

    # Afficher le graphique des incidents par mois
    graphique_incidents_par_mois(data_par_mois)
