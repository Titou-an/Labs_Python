from utils_ne_pas_supprimer import TestSuite, TestCaseWholeFile

test = TestSuite()

file = "exercice6"

cas1 = TestCaseWholeFile(
    test_name="Test1: 1+1j, 1+1j",
    filename=file,
    mock_input=[1+1j, 1+1j],
    expected_output=["La somme est de: (2+2j)","La somme est un réel pur: False", 
    "Le produit est de: 2j", "Le produit est un imaginaire pur: True", "Le module du produit est de: 2.0", 
    "La partie entière du module du produit en binaire est de: 0b10", "La partie entière du module du produit en hexadecimal est de: 0x2"],
    timeout=1
)
cas2 = TestCaseWholeFile(
    test_name="Test2: 2j, 1+3j",
    filename=file,
    mock_input=[2j, 1+3j],
    expected_output=["La somme est de: (1+5j)","La somme est un réel pur: False", 
    "Le produit est de: (-6+2j)", "Le produit est un imaginaire pur: False", "Le module du produit est de: 6.32", 
    "La partie entière du module du produit en binaire est de: 0b110", "La partie entière du module du produit en hexadecimal est de: 0x6"],
    timeout=1
)
cas3 = TestCaseWholeFile(
    test_name="Test3: 58.2, 25+13j",
    filename=file,
    mock_input=[58.2, 25+13j],
    expected_output=["La somme est de: (83.2+13j)", "La somme est un réel pur: False", 
    "Le produit est de: (1455+756.6j)", "Le produit est un imaginaire pur: False", "Le module du produit est de: 1639.96", 
    "La partie entière du module du produit en binaire est de: 0b11001100111", "La partie entière du module du produit en hexadecimal est de: 0x667"],
    timeout=1
)
cas4 = TestCaseWholeFile(
    test_name="Test4: 0, 0",
    filename=file,
    mock_input=[0, 0],
    expected_output=["La somme est de: 0j","La somme est un réel pur: True", 
    "Le produit est de: 0j", "Le produit est un imaginaire pur: True", "Le module du produit est de: 0.0", 
    "La partie entière du module du produit en binaire est de: 0b0", "La partie entière du module du produit en hexadecimal est de: 0x0"],
    timeout=1
)
cas5 = TestCaseWholeFile(
    test_name="Test5: -12+1j, 21-1j",
    filename=file,
    mock_input=[-12+1j, 21-1j],
    expected_output=["La somme est de: (9+0j)","La somme est un réel pur: True", 
    "Le produit est de: (-251+33j)", "Le produit est un imaginaire pur: False", "Le module du produit est de: 253.16", 
    "La partie entière du module du produit en binaire est de: 0b11111101", "La partie entière du module du produit en hexadecimal est de: 0xfd"],
    timeout=1
)
cas6 = TestCaseWholeFile(
    test_name="Test6: -10-43j, -300-46j",
    filename=file,
    mock_input=[-10-43j, -300-46j],
    expected_output=["La somme est de: (-310-89j)","La somme est un réel pur: False", 
    "Le produit est de: (1022+13360j)", "Le produit est un imaginaire pur: False", "Le module du produit est de: 13399.03", 
    "La partie entière du module du produit en binaire est de: 0b11010001010111", "La partie entière du module du produit en hexadecimal est de: 0x3457"],
    timeout=1
)


test.add_tests_cases(cas1, cas2, cas3, cas4, cas5, cas6)

# run la série de test
test()