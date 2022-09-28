from utils_ne_pas_supprimer import run_test, TestCaseWholeFile, Equal

SOURCE_FILE = "exercice3"

TEST_CASES = [
    ("aa", "a", "a"),
    ("ab", "a", "b"),
    ("abc", "ac", "b"),
    ("aclhlaot", "allo", "chat"),
    ("JJ'ea dsouries  muann gjeory euunxe  lpuoriorne..", "J'adore manger une poire.",
     "Je suis un joyeux luron."),
    ("CCeo mnm'ee svto upsa sê tleas  pcehianrem.a.n.t. .!.",
     "Ce n'est pas la peine......", "Comme vous êtes charmant !", ),
    ("ENdegvaerr mAolrlea n!  P.o.e. .?.", "Edgar Allan Poe ?", "Nevermore ! .....")
]

for text, word_1, word_2 in TEST_CASES:
    TestCaseWholeFile(
        test_name=f"text = {text}",
        filename=SOURCE_FILE,
        mock_input=[text],
        expected_output=[
            Equal(f"Votre mot 1 est : \"{word_1}\""),
            Equal(f"Votre mot 2 est : \"{word_2}\""),
        ],
        timeout=1,
        fail_message="Vérifier votre programme"
    )

if __name__ == "__main__" :
    run_test()
