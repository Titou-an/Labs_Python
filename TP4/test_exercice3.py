from utils_ne_pas_supprimer import AlmostEqualNumber, TestCaseWholeFile, Equal, run_test

fichier="exercice3"


TestCaseWholeFile(
    test_name="Exemple1", 
    filename=fichier, 
    mock_input=["1 2 3 4 1 2 3"], 
    expected_output=[AlmostEqualNumber("0.023640543021591385 0.06426165851049616 0.17468129859572226 0.4748329997443803 0.023640543021591385 0.06426165851049616 0.17468129859572226", [5 for _ in range(7)])]
)

TestCaseWholeFile(
    test_name="Exemple2", 
    filename=fichier, 
    mock_input=["-4 0 4"], 
    expected_output=[AlmostEqualNumber("0.0003293204389638929 0.017980286735531547 0.9816903928255045", [5 for _ in range(3)])]
)

TestCaseWholeFile(
    test_name="Exemple3", 
    filename=fichier, 
    mock_input=["0 0 0"], 
    expected_output=[AlmostEqualNumber("0.3333333333333333 0.3333333333333333 0.3333333333333333", [5 for _ in range(3)])]
)

TestCaseWholeFile(
    test_name="Exemple4", 
    filename=fichier, 
    mock_input=["1 0 1 0 1 0 1"], 
    expected_output=[AlmostEqualNumber("0.19593864937345473 0.0720818008353937 0.19593864937345473 0.0720818008353937 0.19593864937345473 0.0720818008353937 0.19593864937345473", [5 for _ in range(7)])]
)

TestCaseWholeFile(
    test_name="Exemple5", 
    filename=fichier, 
    mock_input=["14"], 
    expected_output=[Equal("1.0")]
)

if __name__ == "__main__":
    run_test()