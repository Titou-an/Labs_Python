from utils_ne_pas_supprimer import run_test, TestCaseWholeFile, Equal


file = "exercice2"

TestCaseWholeFile(
    test_name="Exemple 1",
    filename=file,
    mock_input=["casquette avion chandail bateau", "bateau pantalon avion casquette", "casquette avion bateau lunette"],
    expected_output=[
        Equal("avion bateau casquette"),
    ]
)

TestCaseWholeFile(
    test_name="Exemple minuscule majuscule",
    filename=file,
    mock_input=["plante Fleur aRbre", "arbrE fleur lampe", "tapis chaire LampE Fleur ArbRE"],
    expected_output=[
        Equal("arbre fleur"),
    ]
)

TestCaseWholeFile(
    test_name="Exemple 2",
    filename=file,
    mock_input=["casquette avion chandail", "lunette", "lunette"],
    expected_output=[
    ]
)

TestCaseWholeFile(
    test_name="Test vide",
    filename=file,
    mock_input=["", "", ""],
    expected_output=[
    ]
)

TestCaseWholeFile(
    test_name="Test vide2",
    filename=file,
    mock_input=["1 2 3", "4 5 6", "7 8 9"],
    expected_output=[
    ]
)


TestCaseWholeFile(
    test_name="Test ordre",
    filename=file,
    mock_input=["1 2 3", "3 2 1", "2 3 1"],
    expected_output=[
        Equal("1 2 3")
    ]
)

TestCaseWholeFile(
    test_name="Test ordre",
    filename=file,
    mock_input=["1 2 3", "3 2 1", "2 3 1"],
    expected_output=[
        Equal("1 2 3")
    ]
)

if __name__ == "__main__":
    run_test()