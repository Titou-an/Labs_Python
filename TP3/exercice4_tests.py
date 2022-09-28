import random
from utils_ne_pas_supprimer import TestCaseWholeFile, Equal, run_test

SOURCE_FILE = "exercice4"


def get_n_bouteilles_buvables(
    n_bouteilles_vides,
    n_bouteilles_pleines,
    n_bouteilles_echangeables
):
    """Il s'agit de la solution analytique"""
    return n_bouteilles_pleines + \
        (n_bouteilles_pleines + n_bouteilles_vides -
            1) // (n_bouteilles_echangeables - 1)


def get_n_bouteilles_vides_fin(
    n_bouteilles_vides,
    n_bouteilles_pleines,
    n_bouteilles_echangeables
):
    """Il s'agit de la solution analytique"""
    n_bouteilles_buvables = get_n_bouteilles_buvables(
        n_bouteilles_vides,
        n_bouteilles_pleines,
        n_bouteilles_echangeables
    )
    return (n_bouteilles_buvables + n_bouteilles_vides) % n_bouteilles_echangeables


random.seed(0)  # Make all results reproductible

n_tests = 25

n_bouteilles_vides_arr = [0, 1, 0] + \
    [random.randint(0, 2000) for _ in range(n_tests)]
n_bouteilles_pleines_arr = [0, 0, 1] + \
    [random.randint(0, 2000) for _ in range(n_tests)]
n_bouteilles_echangeables_arr = [2, 2, 2] + \
    [random.randint(2, 100) for _ in range(n_tests)]
n_bouteilles_buvables_arr = [0, 0, 1] + \
    [get_n_bouteilles_buvables(
        n_bouteilles_vides_arr[i],
        n_bouteilles_pleines_arr[i],
        n_bouteilles_echangeables_arr[i]
    ) for i in range(len(n_bouteilles_vides_arr) - n_tests, len(n_bouteilles_vides_arr))]
n_bouteilles_vides_fin_arr = [0, 1, 1] + \
    [get_n_bouteilles_vides_fin(
        n_bouteilles_vides_arr[i],
        n_bouteilles_pleines_arr[i],
        n_bouteilles_echangeables_arr[i]
    ) for i in range(len(n_bouteilles_vides_arr) - n_tests, len(n_bouteilles_vides_arr))]

for i in range(len(n_bouteilles_vides_arr)):

    n_bouteilles_vides = n_bouteilles_vides_arr[i]
    n_bouteilles_pleines = n_bouteilles_pleines_arr[i]
    n_bouteilles_echangeables = n_bouteilles_echangeables_arr[i]
    n_bouteilles_buvables = n_bouteilles_buvables_arr[i]
    n_bouteilles_vides_fin = n_bouteilles_vides_fin_arr[i]

    TestCaseWholeFile(
        test_name=f"n_bouteilles_vides = {n_bouteilles_vides}"
        f", n_bouteilles_pleines = {n_bouteilles_pleines}"
        f", n_bouteilles_echangeables = {n_bouteilles_echangeables}",
        filename=SOURCE_FILE,
        mock_input=[
            f"{n_bouteilles_vides}",
            f"{n_bouteilles_pleines}",
            f"{n_bouteilles_echangeables}",
        ],
        expected_output=[
            Equal(
                f"Vous pouvez boire exactement {n_bouteilles_buvables} bouteille(s)"),
            Equal(
                f"Il vous restera {n_bouteilles_vides_fin} bouteille(s) vide(s) a la fin")
        ],
        timeout=1,
        fail_message="Vérifier votre programme"
    )

if __name__ == "__main__" :
    run_test()
