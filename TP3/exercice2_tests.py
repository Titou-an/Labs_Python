from utils_ne_pas_supprimer import run_test, TestCaseWholeFile, Equal

SOURCE_FILE = "exercice2"

LOREM_TEXT = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
LOREM_TEXT_KEY = 10
LOREM_TEXT_ENCRYPTED = "Vybow Szcew sc cswzvi newwi dohd yp dro zbsxdsxq kxn dizocoddsxq sxnecdbi. Vybow Szcew rkc loox dro sxnecdbi'c cdkxnkbn newwi dohd ofob csxmo dro 1500c, grox kx exuxygx zbsxdob dyyu k qkvvoi yp dizo kxn cmbkwlvon sd dy wkuo k dizo czomswox lyyu. Sd rkc cebfsfon xyd yxvi psfo moxdebsoc, led kvcy dro vokz sxdy ovomdbyxsm dizocoddsxq, bowksxsxq occoxdskvvi exmrkxqon. Sd gkc zyzevkbscon sx dro 1960c gsdr dro bovokco yp Vodbkcod croodc myxdksxsxq Vybow Szcew zkcckqoc, kxn wybo bomoxdvi gsdr nocudyz zelvscrsxq cypdgkbo vsuo Kvnec ZkqoWkuob sxmvensxq fobcsyxc yp Vybow Szcew."

TEST_CASES = [
    ("", 3, ""),
    ("Allo poly", 3, "Door srob"),
    ("bonjour les jeunes", 3, "erqmrxu ohv mhxqhv"),
    ("bonjour les jeunes", 70, "tgfbgmj dwk bwmfwk"),
    ("bonjour les Jeunes", 3, "erqmrxu ohv Mhxqhv"),
    ("Bonjour les jeunes", 70, "Tgfbgmj dwk bwmfwk"),
    ("Ceci est un$test#%", 6, "Ikio kyz at$zkyz#%"),
    ("01234aaa$$$", 19, "01234ttt$$$"),
    (LOREM_TEXT, LOREM_TEXT_KEY, LOREM_TEXT_ENCRYPTED)
]

for text, key, text_encrypted in TEST_CASES:
    # Tests with alphanumeric strings
    TestCaseWholeFile(
        test_name=f"Texte = \"{text}\", Cle = {key}",
        filename=SOURCE_FILE,
        mock_input=[text, str(key)],
        expected_output=[
            Equal(f"Votre texte chiffre est : \"{text_encrypted}\"")
        ],
        timeout=1,
        fail_message="Vérifier votre programme"
    )

if __name__ == "__main__":
    run_test()
