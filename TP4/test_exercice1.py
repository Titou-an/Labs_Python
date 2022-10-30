from utils_ne_pas_supprimer import run_test, TestCaseWholeFile, Equal

file = "exercice1"

TestCaseWholeFile(
    test_name="Test anagramme avec majuscule",
    filename=file,
    mock_input=["Monsieur Jack, vous dactylographiez bien mieux que Wolf"],
    expected_output=[
        Equal("[]"),
        Equal("{'a': ['dactylographiez', 'jack,'], 'b': ['bien'], 'c': ['dactylographiez', 'jack,'], 'd': ['dactylographiez'], 'e': ['bien', 'dactylographiez', 'mieux', 'monsieur', 'que'], 'f': ['wolf'], 'g': ['dactylographiez'], 'h': ['dactylographiez'], 'i': ['bien', 'dactylographiez', 'mieux', 'monsieur'], 'j': ['jack,'], 'k': ['jack,'], 'l': ['dactylographiez', 'wolf'], 'm': ['mieux', 'monsieur'], 'n': ['bien', 'monsieur'], 'o': ['dactylographiez', 'monsieur', 'vous', 'wolf'], 'p': ['dactylographiez'], 'q': ['que'], 'r': ['dactylographiez', 'monsieur'], 's': ['monsieur', 'vous'], 't': ['dactylographiez'], 'u': ['mieux', 'monsieur', 'que', 'vous'], 'v': ['vous'], 'w': ['wolf'], 'x': ['mieux'], 'y': ['dactylographiez'], 'z': ['dactylographiez']}")
    ],
    fail_message="Verifiez que vous gerez les majuscules"
)

TestCaseWholeFile(
    test_name="Test anagramme minuscule",
    filename=file,
    mock_input=["monsieur jack, vous dactylographiez bien mieux que wolf"],
    expected_output=[
        Equal("[]"),
        Equal("{'a': ['dactylographiez', 'jack,'], 'b': ['bien'], 'c': ['dactylographiez', 'jack,'], 'd': ['dactylographiez'], 'e': ['bien', 'dactylographiez', 'mieux', 'monsieur', 'que'], 'f': ['wolf'], 'g': ['dactylographiez'], 'h': ['dactylographiez'], 'i': ['bien', 'dactylographiez', 'mieux', 'monsieur'], 'j': ['jack,'], 'k': ['jack,'], 'l': ['dactylographiez', 'wolf'], 'm': ['mieux', 'monsieur'], 'n': ['bien', 'monsieur'], 'o': ['dactylographiez', 'monsieur', 'vous', 'wolf'], 'p': ['dactylographiez'], 'q': ['que'], 'r': ['dactylographiez', 'monsieur'], 's': ['monsieur', 'vous'], 't': ['dactylographiez'], 'u': ['mieux', 'monsieur', 'que', 'vous'], 'v': ['vous'], 'w': ['wolf'], 'x': ['mieux'], 'y': ['dactylographiez'], 'z': ['dactylographiez']}")
    ]
)

TestCaseWholeFile(
    test_name="Test avec w manquant",
    filename=file,
    mock_input=["Monsieur Jack, vous dactylographiez bien mieux que olf"],
    expected_output=[
        Equal("['w']"),
        Equal("{'a': ['dactylographiez', 'jack,'], 'b': ['bien'], 'c': ['dactylographiez', 'jack,'], 'd': ['dactylographiez'], 'e': ['bien', 'dactylographiez', 'mieux', 'monsieur', 'que'], 'f': ['olf'], 'g': ['dactylographiez'], 'h': ['dactylographiez'], 'i': ['bien', 'dactylographiez', 'mieux', 'monsieur'], 'j': ['jack,'], 'k': ['jack,'], 'l': ['dactylographiez', 'olf'], 'm': ['mieux', 'monsieur'], 'n': ['bien', 'monsieur'], 'o': ['dactylographiez', 'monsieur', 'olf', 'vous'], 'p': ['dactylographiez'], 'q': ['que'], 'r': ['dactylographiez', 'monsieur'], 's': ['monsieur', 'vous'], 't': ['dactylographiez'], 'u': ['mieux', 'monsieur', 'que', 'vous'], 'v': ['vous'], 'w': [], 'x': ['mieux'], 'y': ['dactylographiez'], 'z': ['dactylographiez']}")
    ]
)

TestCaseWholeFile(
    test_name="salut",
    filename=file,
    mock_input=["salut"],
    expected_output=[
        Equal("['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 'v', 'w', 'x', 'y', 'z']"),
        Equal("{'a': ['salut'], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': ['salut'], 'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': ['salut'], 't': ['salut'], 'u': ['salut'], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}")
    ]
)

TestCaseWholeFile(
    test_name="vide",
    filename=file,
    mock_input=[""],
    expected_output=[
        Equal("['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']"),
        Equal("{'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [], 'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}")
    ]
)


if __name__ == "__main__":
    run_test()