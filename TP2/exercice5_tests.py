from utils_ne_pas_supprimer import TestSuite, TestCaseWholeFile

test = TestSuite()

file = "exercice5"

cas1 = TestCaseWholeFile(
    test_name="Test1: 274.25, 12, 9",
    filename=file,
    mock_input=[274.25, 12, 9],
    expected_output=["---- Calculateur de pourboire ----","Pourboire total: $ 32.91", "Pourboire par membre: $ 3.66", "--- Coût total ---","Facture totale: $ 307.16", "Chacun doit payer: $ 34.13"],
    timeout=1
)
cas2 = TestCaseWholeFile(
    test_name="Test2: 38, 15, 3",
    filename=file,
    mock_input=[38, 15, 3],
    expected_output=["---- Calculateur de pourboire ----","Pourboire total: $ 5.7", "Pourboire par membre: $ 1.9", "--- Coût total ---","Facture totale: $ 43.7", "Chacun doit payer: $ 14.57"],
    timeout=1
)
cas3 = TestCaseWholeFile(
    test_name="Test3: 22.65, 10, 1",
    filename=file,
    mock_input=[22.65, 10, 1],
    expected_output=["---- Calculateur de pourboire ----","Pourboire total: $ 2.27", "Pourboire par membre: $ 2.27", "--- Coût total ---","Facture totale: $ 24.91", "Chacun doit payer: $ 24.91"],
    timeout=1
)
cas4 = TestCaseWholeFile(
    test_name="Test4: 150, 12, 5",
    filename=file,
    mock_input=[150, 12, 5],
    expected_output=["---- Calculateur de pourboire ----","Pourboire total: $ 18.0", "Pourboire par membre: $ 3.6", "--- Coût total ---","Facture totale: $ 168.0", "Chacun doit payer: $ 33.6"],
    timeout=1
)
cas5 = TestCaseWholeFile(
    test_name="Test5: 78, 10, 3",
    filename=file,
    mock_input=[78, 10, 3],
    expected_output=["---- Calculateur de pourboire ----","Pourboire total: $ 7.8", "Pourboire par membre: $ 2.6", "--- Coût total ---","Facture totale: $ 85.8", "Chacun doit payer: $ 28.6"],
    timeout=1
)


test.add_tests_cases(cas1, cas2, cas3, cas4, cas5)

# run la série de test
test()