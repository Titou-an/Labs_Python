from utils_ne_pas_supprimer import TestCaseWholeFile, Equal, run_test
fichier="exercice5"


TestCaseWholeFile(
    test_name="Exemple 1",
    filename=fichier,
    mock_input=['1 2 3 4 5 1', '3'],
    expected_output=[Equal('1 est un doublon dans la liste et la somme des index est supérieure à 3')]
)

TestCaseWholeFile(
    test_name="Exemple 2",
    filename=fichier,
    mock_input=['1 1 2 3 4', '5'],
    expected_output=[Equal("Il n'y a pas de doublons tels la somme des index est supérieure à 5")]
)

TestCaseWholeFile(
    test_name="Exemple 3",
    filename=fichier,
    mock_input=['1 2 3 4 5', '2'],
    expected_output=[Equal("Il n'y a pas de doublons tels la somme des index est supérieure à 2")]
)

TestCaseWholeFile(
    test_name="Exemple plusieurs duplicats",
    filename=fichier,
    mock_input=['2 2 1 3 4 1', '4'],
    expected_output=[Equal("1 est un doublon dans la liste et la somme des index est supérieure à 4")]
)

TestCaseWholeFile(
    test_name="Exemple plusieurs memes duplicats",
    filename=fichier,
    mock_input=['2 2 3 4 2 2 2', '6'],
    expected_output=[Equal("2 est un doublon dans la liste et la somme des index est supérieure à 6")]
)

TestCaseWholeFile(
    test_name="Exemple prendre plus grands indices",
    filename=fichier,
    mock_input=['9 18 0 14 18 7 4 8 29 81 18', '7'],
    expected_output=[Equal("18 est un doublon dans la liste et la somme des index est supérieure à 7")]
)

TestCaseWholeFile(
    test_name="Exemple plusieurs nombres valides",
    filename=fichier,
    mock_input=['1 2 1 2 1', '2'],
    expected_output=[Equal("1 est un doublon dans la liste et la somme des index est supérieure à 2")]
)

if __name__ == "__main__":
    run_test()