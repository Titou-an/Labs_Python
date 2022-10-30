from utils_ne_pas_supprimer import TestCaseWholeFile, Equal, run_test
fichier="exercice9"

TestCaseWholeFile(
    test_name="Exemple 1",
    filename=fichier,
    mock_input=["Francois Jean Martin Stephane Alexandre Joseph", "Francois Mike Martin Stephane Claude Jacques"], 
    expected_output=[Equal("Les professeurs suivants enseignent un seul des deux projets: ['Alexandre', 'Claude', 'Jacques', 'Jean', 'Joseph', 'Mike']")]
)

TestCaseWholeFile(
    test_name="Exemple 2",
    filename=fichier,
    mock_input=["Francois Jean Martin Stephane Alexandre Joseph", "Francois Jean Martin Stephane Alexandre"], 
    expected_output=[Equal("Joseph est le seul professeur qui enseigne un seul des deux projets.")]
)

TestCaseWholeFile(
    test_name="Exemple 3",
    filename=fichier,
    mock_input=["Francois Jean Martin Stephane Alexandre Joseph", "Francois Jean Martin Stephane Alexandre Maxime"], 
    expected_output=[Equal("Joseph et Maxime sont les professeurs qui enseignent un seul des deux projets.")]
)

TestCaseWholeFile(
    test_name="Exemple 4",
    filename=fichier,
    mock_input=["Francois Jean Martin Stephane Alexandre Joseph", "Francois Jean Martin Stephane Alexandre Joseph"], 
    expected_output=[Equal("Il n'y a pas de professeurs qui enseignent un seul des deux projets.")]
)

TestCaseWholeFile(
    test_name="Test liste vide",
    filename=fichier,
    mock_input=["", ""], 
    expected_output=[Equal("Il n'y a pas de professeurs qui enseignent un seul des deux projets.")]
)

TestCaseWholeFile(
    test_name="Test majuscule minuscule",
    filename=fichier,
    mock_input=["daniel martine", "DANIeL martine"], 
    expected_output=[Equal("DANIeL et daniel sont les professeurs qui enseignent un seul des deux projets.")]
)

if __name__ == "__main__":
    run_test()