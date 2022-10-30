from utils_ne_pas_supprimer import TestCaseWholeFile, Equal, run_test
fichier="exercice6"

TestCaseWholeFile(
    test_name="Test vide",
    filename=fichier,
    mock_input=[""], 
    expected_output=[Equal("Il n'y a pas de doublons")]
)

TestCaseWholeFile(
    test_name="Exemple 1 : Un doublon",
    filename=fichier,
    mock_input=['test test bonsoir poly'],
    expected_output=[Equal('Il y a 1 doublon')]
)


TestCaseWholeFile(
    test_name="Exemple 2 : Test deux doublons",
    filename=fichier,
    mock_input=['test test bonsoir bonsoir mtl'],
    expected_output=[Equal('Il y a 2 doublons')]
)


TestCaseWholeFile(
    test_name="Exemple 3 : Test pas de doublons",
    filename=fichier,
    mock_input=['poly mtl autonme'],
    expected_output=[Equal("Il n'y a pas de doublons")]
)

TestCaseWholeFile(
    test_name="Test plusieurs doublons",
    filename=fichier,
    mock_input=['a c b d b d a c'],
    expected_output=[Equal("Il y a 4 doublons")]
)

if __name__ == "__main__":
    run_test()