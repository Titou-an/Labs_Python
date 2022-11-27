"""
exercice1.py
Exercice 1 du TP6 du cours INF1005D
Description : Programme qui permet d'apprendre les bases de la librairie Numpy.
Auteurs     : William Morin (2213763), Théo Manach (2058412)
"""

import numpy as np


def example_matrix():
    """Fonction qui génère une matrice 3x4 qui contient les valeurs suivantes:
    [8, 2, 142, 4]
    [1, 5, 2, 5]
    [1, 1, 23, 145]

    Paramètres de la fonction :
        Aucun.

    Valeur de retour :
        Une matrice numpy de taille 3x4 contenant les valeurs ci-dessus.
    """

    # Retirez "pass" et écrivez votre code ici
    return np.array([[8, 2, 142, 4],
                     [1, 5, 2, 5],
                     [1, 1, 23, 145]])


def matrix_of_ones(n):
    """Fonction qui génère une matrice de taille n x n qui ne contient que la valeur 1, 
       sauf à la 1ère ligne, 2e colonne où la valeur est 5.

    Si n <= 1, cette opération est impossible. Votre code doit donc retourner None.

    Exemple:
    #>>> matrix_of_ones(4)
        array([[1., 5., 1., 1.],
               [1., 1., 1., 1.],
               [1., 1., 1., 1.],
               [1., 1., 1., 1.]])
    #>>> matrix_of_ones(1)
        None

    Conseil: la fonction 'np.ones(...)' peut être très utile.

    Paramètres de la fonction :
        n (int) : taille de la matrice

    Valeur de retour :
        Une matrice numpy de taille n x n ayant les caractéristiques décrites ci-dessus, ou None si n <= 1.
    """
    # Retirez "pass" et écrivez votre code ici

    if not n <= 1:
        a = np.ones((n, n))
        a[0, 1] = 5
        return a
    else:
        return None


def third_column(matrix):
    """Fonction pour aller chercher la 3e colonne d'une matrice carré de taille n par n, où n >= 3.

    Paramètres de la fonction :
        matrix (np.ndarray) : matrice d'entrée.

    Valeur de retour :
        Un vecteur numpy qui contient la 3e colonne de la matrice.
    """

    # Retirez "pass" et écrivez votre code ici

    if np.shape(matrix)[0] >= 3:
        if np.shape(matrix)[0] == np.shape(matrix)[1]:
            return matrix[:, 2]

    return None


def first_row(matrix):
    """Fonction pour aller chercher la 1ère ligne d'une matrice carré de taille n par n, où n >= 2.

    Paramètres de la fonction :
        matrix (np.ndarray) : matrice d'entrée.

    Valeur de retour :
        Un vecteur numpy qui contient la 1ère ligne de la matrice.
    """

    # Retirez "pass" et écrivez votre code ici

    if matrix.shape[0] >= 2:
        if matrix.shape[0] == matrix.shape[1]:
            return matrix[0]

    return None


def array_size(array):
    """Fonction permettant d'obtenir le nombre d'éléments dans une matrice.

    Exemple:
        Pour une matrice d'entrée suivante:
        [1 2 3 4]
        [5 6 7 8]
        [9 8 7 6]
        [1 2 5 6]
        Le nombre d'éléments serait 4*4=16.

    Paramètres de la fonction :
        matrix (np.ndarray) : matrice d'entrée.

    Valeur de retour :
        int : nombre d'éléments dans la matrice.
    """

    # Retirez "pass" et écrivez votre code ici

    return array.size


def array_max_and_index(array):
    """Fonction permettant de trouver la valeur maximale d'un vecteur ainsi que la position de cette valeur dans le vecteur.

    Attention! Vous ne pouvez pas utiliser de boucles. Vous devez utiliser les fonctions numpy.

    Exemple:
        Pour le vecteur numpy suivant: array([7, 9, 12, 4, 0, 1])
        On cherche à obtenir le tuple suivant: (12, 2)

    Paramètres de la fonction :
        array (np.ndarray) : vecteur de type numpy.

    Valeur de retour :
        un tuple contenant les valeurs suivantes: (valeur_max, position_valeur_max)
    """

    # Retirez "pass" et écrivez votre code ici

    return (array.max(), np.where(array == array.max())[0][0])


def array_of_equidistant_points():
    """Fonction qui génère un vecteur qui contient 6 points équidistants entre 0 et 30 (inclusivement).

    Paramètres de la fonction :
        Aucun.

    Valeur de retour :
        Un vecteur numpy (np.ndarray) de longueur 6 ayant les valeurs décrites ci-dessus.
    """

    # Retirez "pass" et écrivez votre code ici

    return np.arange(0, 31, 6)


def top_right_array_elements(matrix):
    """Fonction pour aller chercher une sous-matrice 2x2 (dans le coin supérieur droit) d'une matrice carré.

    Vous devrez utilisez la notation d'indexage en deux dimensions.
    Vous n'avez pas le droit d'utiliser de boucles.

    Exemple:
        Pour une matrice d'entrée suivante:
        [1 2 3 4]
        [5 6 7 8]
        [9 8 7 6]
        [1 2 5 6]
        On cherche à obtenir:
        [3 4]
        [7 8]

    Paramètres de la fonction :
        matrix (np.ndarray) : matrice d'entrée de forme carré.

    Valeur de retour :
        Une matrice numpy de taille 2x2 contenant les éléments dans le coin supérieur droit de la matrice.
    """

    # Retirez "pass" et écrivez votre code ici
    return np.array([[matrix[0, -2], matrix[0, -1]], [matrix[1, -2], matrix[1, -1]]])


def multiplier_matrices(matrix_a, matrix_b):
    """Fonction qui multiplie deux matrices ensemble.
    On parle ici du produit scalaire.

    Attention! Vous devez valider que l'opération est possible avant de l'effectuer.
    Si les tailles des matrices ne permettent pas la multiplication, vous devrez retourner None.

    Conseil: La fonction numpy "np.dot(...)" pourra vous aider.

    Paramètres de la fonction :
        matrix_a (np.ndarray) : La matrice A
        matrix_b (np.ndarray) : La matrice B

    Valeur de retour :
        Une matrice numpy (np.ndarray) qui contient le résultat de la multiplication AB ou None si impossible.
    """

    # Retirez "pass" et écrivez votre code ici

    if matrix_a.shape[1] == matrix_b.shape[0]:
        return np.dot(matrix_a, matrix_b)
    else:
        return None


def solve_system():
    """Fonction qui résout le système d'équation expliqué dans l'énoncé du TP (voir PDF).

    Vous devrez effectuer une résolution d'un système matriciel.
    Heureusement, avec numpy, cela est très simple. 
    Conseil: La fonction numpy 'np.linalg.solve' pourra vous aider. Vous devez seulement donner deux paramètres à cette fonction.

    Paramètres de la fonction :
        Aucun.

    Valeur de retour :
        Un vecteur numpy (np.ndarray) qui contient le point x, y, z de l'intersection des trois plans.
    """

    # Retirez "pass" et écrivez votre code ici

    coefficients = np.matrix([[-3, -1, 1],
                              [-1, -4, 1],
                              [-0.1, -1, 1]])
    dependantes = np.array([1, -1, 0])
    return np.linalg.solve(coefficients,dependantes)


if __name__ == "__main__":
    # Ne modifiez pas cette section
    # Elle permet de tester vos fonctions :-)

    print("Matrice exemple:\n", example_matrix())

    print("Matrice de 1:\n", matrix_of_ones(4))
    A = np.array([[1, 2], [4, 1]])
    print("Nombre d'éléments dans la matrice A: ", array_size(A))

    vecteur = np.array([9, 1, 0, 4, 3, 19, 0, 1])
    print("Maximum d'un vecteur et l'index: ", array_max_and_index(vecteur))

    print("Liste de 6 points équidistants entre 0 et 30:\n", array_of_equidistant_points())

    B = np.array([[1, 2, 1, 9],
                  [3, 4, 3, 9],
                  [4, 9, 1, 10],
                  [1, 4, 5, 0]])
    print("Matrice 2x2 du coin supérieur droit de la matrice B:\n", top_right_array_elements(B))

    print("3e colonne de la matrice B:\n", third_column(B))
    print("1ère ligne de la matrice B:\n", first_row(B))

    C = np.array([[1, 3], [4, 5]])
    D = np.array([[0, 1], [4, 1]])
    print("Multiplication de C et D:\n", multiplier_matrices(C, D))

    print("Point d'intersection des trois plans: (x, y, z) =", solve_system())
