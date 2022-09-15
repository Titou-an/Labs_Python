from utils_ne_pas_supprimer import TestSuite, TestCaseWholeFile

test = TestSuite()

file = "exercice1"

for n in range(10):
    # Ici j'utillise la multiplication pour eviter que les eleves viennent dans ce fichier pour trouver la solution
    expected = n + n * n + n * n * n
    cas = TestCaseWholeFile(
        test_name=f"Test{n + 1}",
        filename=file,
        mock_input=[n],
        expected_output=["Le résultat est : " + str(expected)],
        timeout=1
    )
    test.add_tests_cases(cas)

test()