from utils_ne_pas_supprimer import TestCaseWholeFile, Equal, run_test
fichier="exercice8"

TestCaseWholeFile(
    test_name="Exemple 1",
    filename=fichier,
    mock_input=["2 5 1 6 9 3", "9"], 
    expected_output=[Equal("Les nombres aux indexes 3 et 5 ont une somme de 9")]
)

TestCaseWholeFile(
    test_name="Exemple 2",
    filename=fichier,
    mock_input=["1 2 3 4 5 6", "20"], 
    expected_output=[Equal("Il n'y a aucune paire de nombres dans la liste dont la somme donne 20")]
)

TestCaseWholeFile(
    test_name="Petite liste",
    filename=fichier,
    mock_input=["1 1", "2"], 
    expected_output=[Equal("Les nombres aux indexes 0 et 1 ont une somme de 2")]
)

TestCaseWholeFile(
    test_name="Tres longue liste",
    filename=fichier,
    mock_input=["10 1 2 3 4 65 7 4 2 1 6 34 2 5 7 54 3 2 4 6 77 6 4 3 2 1 4 5 65 6 9 8 7 6 5 43 3 56 7 8 254", "264"], 
    expected_output=[Equal("Les nombres aux indexes 0 et 40 ont une somme de 264")]
)

TestCaseWholeFile(
    test_name="Test",
    filename=fichier,
    mock_input=["9 8 7 1 2 4 1 ", "5"], 
    expected_output=[Equal("Les nombres aux indexes 3 et 5 ont une somme de 5")]
)

if __name__ == "__main__":
    run_test()