from utils_ne_pas_supprimer import TestSuite, TestCaseWholeFile

test = TestSuite()

file = "exercice3"


cas1 = TestCaseWholeFile(
    test_name="Test1: '11', '5', '-7', '2'",
    filename=file,
    mock_input=['11', '5', '-7', '2'],
    expected_output=["La distance minimale est de 7.28"],
    timeout=1
)
cas2 = TestCaseWholeFile(
    test_name="Test2: '0', '0', '0', '0'",
    filename=file,
    mock_input=['0', '0', '0', '0'],
    expected_output=["La distance minimale est de 0.0"],
    timeout=1
)
cas3 = TestCaseWholeFile(
    test_name="Test3: '80', '-140', '-45', '90'",
    filename=file,
    mock_input=['80', '-140', '-45', '90'],
    expected_output=["La distance minimale est de 100.62"],
    timeout=1
)

test.add_tests_cases(cas1, cas2, cas3)
test()