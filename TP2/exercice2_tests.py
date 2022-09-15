from utils_ne_pas_supprimer import TestSuite, TestCaseWholeFile

test = TestSuite()

file = "exercice2"

cas1 = TestCaseWholeFile(
    test_name="Test1: '12', '4', '2000'",
    filename=file,
    mock_input=['12', '4', '2000'],
    expected_output=["L'utilisateur est né le 12-04-2000 et il aura 22 ans à la fin de l'année."],
    timeout=1
)
cas2 = TestCaseWholeFile(
    test_name="Test2: '25', '12', '1950'",
    filename=file,
    mock_input=['25', '12', '1950'],
    expected_output=["L'utilisateur est né le 25-12-1950 et il aura 72 ans à la fin de l'année."],
    timeout=1
)
cas3 = TestCaseWholeFile(
    test_name="Test3: '31', '12', '1900'",
    filename=file,
    mock_input=['31', '12', '1900'],
    expected_output=["L'utilisateur est né le 31-12-1900 et il aura 122 ans à la fin de l'année."],
    timeout=1
)

test.add_tests_cases(cas1, cas2, cas3)
test()