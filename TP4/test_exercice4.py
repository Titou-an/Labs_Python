from utils_ne_pas_supprimer import TestCaseWholeFile, Equal, run_test
fichier="exercice4"


TestCaseWholeFile(
    test_name="Exemple 1",
    filename=fichier,
    mock_input=['-1', '2', 'Marcel', '17', 'Leboeuf', '4'], 
    expected_output=[Equal("('Leboeuf', 4)"), Equal("('Marcel', 17)")]
)

TestCaseWholeFile(
    test_name="Exemple 2",
    filename=fichier,
    mock_input=['3', 'Marcel', '22', '-1', '15', 'Moi', '45', '20', 'Toi', '77', '-55', '4'],
    expected_output=[Equal("('Toi', 4)"), Equal("('Marcel', 15)"), Equal("('Moi', 20)")]
)

TestCaseWholeFile(
    test_name="Exemple 3",
    filename=fichier,
    mock_input=['4', 'Un', '1', 'Deux', '2', 'Trois', '3', 'Quatre', '4'],
    expected_output=[Equal("('Un', 1)"), Equal("('Deux', 2)"), Equal("('Trois', 3)"), Equal("('Quatre', 4)")]
)

TestCaseWholeFile(
    test_name="Exemple 4",
    filename=fichier,
    mock_input=['4', 'Quatre', '4', 'Trois', '3', 'Deux', '2', 'Un', '1'],
    expected_output=[Equal("('Un', 1)"), Equal("('Deux', 2)"), Equal("('Trois', 3)"), Equal("('Quatre', 4)")]
)

if __name__ == "__main__":
    run_test()