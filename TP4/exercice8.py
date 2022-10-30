"""
exercice8.py
Description : Somme de deux éléments valant k
Auteurs     : Les deux mots ne sont pas des anagrammes
"""

"""
Écrire un programme qui demande aux utilisateurs d'entrer une liste de nombres et qui demande aussi un 
nombre k.

Le programme doit trouver deux elements telle que leur somme est égale à k. Si ces deux éléments sont
trouvés, afficher leurs 2 indexes. 
* Note: Les deux index doivent s'afficher par ordre croissant.
* Note: Il n'est pas nécessaire de faire de la validation d'entrée.

#### Exemples ####
* Note: Les phrases "* Explication: ..." ne devraient pas être affichées par votre programme. 
        Elles sont là pour vous aider à comprendre les exemples.

### Exemple 1:
Veuillez entrer une liste de nombres: 2 5 1 6 9 3
Veuillez entrer le nombre k: 9
Les nombres aux indexes 3 et 5 ont une somme de 9

* Explication: En effet, à l'index 3 on a le nombre 6 et à l'index 5 on a le nombre 3, on a bien 6 + 3 = 9.

### Exemple 2:
Veuillez entrer une liste de nombres: 1 2 3 4 5 6
Veuillez entrer le nombre k: 4
Les nombres aux indexes 0 et 2 ont une somme de 4
* Explication: En effet, à l'index 0 on a le nombre 1 et à l'index 2 on a le nombre 3, on a bien 1 + 4 = 4.

### Exemple 3:
Veuillez entrer une liste de nombres: 4 5 6 1 2 3
Veuillez entrer le nombre k: 20
Il n'y a aucune paire de nombres dans la liste dont la somme donne 20

"""

# TODO: Commencez votre programme ici

liste = list(map(int, input("").split()))
k = int(input("Veuillez entrer le nombre k: "))
index = []

for i in range(len(liste)):
    for j in range(i + 1, len(liste)):
        if liste[i] + liste[j] == k:
            index.extend([i,j])
            break

if len(index) == 0:
    print(f"Il n'y a aucune paire de nombres dans la liste dont la somme donne {k}")
else:
    print(f"Les nombres aux indexes {index[0]} et {index[1]} ont une somme de {k}")