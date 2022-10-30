from utils_ne_pas_supprimer import TestCaseWholeFile, Equal, run_test
fichier="exercice7"


TestCaseWholeFile(
    test_name="Exemple 1",
    filename=fichier,
    mock_input=["manger", "partir"], 
    expected_output=[Equal("Les deux mots ne sont pas des anagrammes")]
)

TestCaseWholeFile(
    test_name="Exemple 2",
    filename=fichier,
    mock_input=["migraine", "imaginer"], 
    expected_output=[Equal("Les deux mots sont des anagrammes")]
)

TestCaseWholeFile(
    test_name="Test mots de taille differente",
    filename=fichier,
    mock_input=["bonjour", "bonjou"], 
    expected_output=[Equal("Les deux mots ne sont pas des anagrammes")]
)

TestCaseWholeFile(
    test_name="Test mots avec memes lettres",
    filename=fichier,
    mock_input=["aaaa", "aaa"], 
    expected_output=[Equal("Les deux mots ne sont pas des anagrammes")]
)

TestCaseWholeFile(
    test_name="Test meme mot",
    filename=fichier,
    mock_input=["kayak", "kayak"], 
    expected_output=[Equal("Les deux mots sont des anagrammes")]
)

if __name__ == "__main__":
    run_test()