from utils_ne_pas_supprimer import TestSuite, TestCaseWholeFile

test = TestSuite()

file = "exercice4"

cas1 = TestCaseWholeFile(
    test_name="Test1: 'Introduction à Python', 33, 3",
    filename=file,
    mock_input=['Introduction à Python', 33, 3],
    expected_output=["----- Planificateur d'étude -----","Le cours Introduction à Python", "A besoin d'un nombre d'heures d'étude de : 99.0 heure(s)", "Le budget d'étude est dépassé: True", "----- Fin de programme, merci et à très bientôt -----"],
    timeout=1
)
cas2 = TestCaseWholeFile(
    test_name="Test2: 'Algèbre linéaire', 28, 2",
    filename=file,
    mock_input=['Algèbre linéaire', 28, 2],
    expected_output=["----- Planificateur d'étude -----","Le cours Algèbre linéaire", "A besoin d'un nombre d'heures d'étude de : 56.0 heure(s)", "Le budget d'étude est dépassé: True", "----- Fin de programme, merci et à très bientôt -----"],
    timeout=1
)
cas3 = TestCaseWholeFile(
    test_name="Test3: 'Comptabilité analytique', 30, 4",
    filename=file,
    mock_input=['Comptabilité analytique', 30, 4],
    expected_output=["----- Planificateur d'étude -----","Le cours Comptabilité analytique", "A besoin d'un nombre d'heures d'étude de : 120.0 heure(s)", "Le budget d'étude est dépassé: True", "----- Fin de programme, merci et à très bientôt -----"],
    timeout=1
)

cas4 = TestCaseWholeFile(
    test_name="Test4: 'Mécanique pour ingénieur', -2, 0.9999",
    filename=file,
    mock_input=['Mécanique pour ingénieur', -2, 0.9999],
    expected_output=["----- Planificateur d'étude -----","Le cours Mécanique pour ingénieur", "A besoin d'un nombre d'heures d'étude de : -1.9998 heure(s)", "Le budget d'étude est dépassé: False", "----- Fin de programme, merci et à très bientôt -----"],
    timeout=1
)

test.add_tests_cases(cas1, cas2, cas3, cas4)

# run la série de test
test()