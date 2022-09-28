import random
from utils_ne_pas_supprimer import Equal, TestCaseWholeFile, run_test

SOURCE_FILE = "exercice5"

DIAMOND_1 = """
.@.
@@@
.@.
"""

DIAMOND_2 = """
..@..
.@@@.
@@@@@
.@@@.
..@..
"""

DIAMOND_3 = """
...@...
..@@@..
.@@@@@.
@@@@@@@
.@@@@@.
..@@@..
...@...
"""

DIAMOND_4 = """
....@....
...@@@...
..@@@@@..
.@@@@@@@.
@@@@@@@@@
.@@@@@@@.
..@@@@@..
...@@@...
....@....
"""

DIAMOND_5 = """
.....@.....
....@@@....
...@@@@@...
..@@@@@@@..
.@@@@@@@@@.
@@@@@@@@@@@
.@@@@@@@@@.
..@@@@@@@..
...@@@@@...
....@@@....
.....@.....
"""

DIAMOND_10 = """
..........@..........
.........@@@.........
........@@@@@........
.......@@@@@@@.......
......@@@@@@@@@......
.....@@@@@@@@@@@.....
....@@@@@@@@@@@@@....
...@@@@@@@@@@@@@@@...
..@@@@@@@@@@@@@@@@@..
.@@@@@@@@@@@@@@@@@@@.
@@@@@@@@@@@@@@@@@@@@@
.@@@@@@@@@@@@@@@@@@@.
..@@@@@@@@@@@@@@@@@..
...@@@@@@@@@@@@@@@...
....@@@@@@@@@@@@@....
.....@@@@@@@@@@@.....
......@@@@@@@@@......
.......@@@@@@@.......
........@@@@@........
.........@@@.........
..........@..........
"""

DIAMOND_20 = """
....................@....................
...................@@@...................
..................@@@@@..................
.................@@@@@@@.................
................@@@@@@@@@................
...............@@@@@@@@@@@...............
..............@@@@@@@@@@@@@..............
.............@@@@@@@@@@@@@@@.............
............@@@@@@@@@@@@@@@@@............
...........@@@@@@@@@@@@@@@@@@@...........
..........@@@@@@@@@@@@@@@@@@@@@..........
.........@@@@@@@@@@@@@@@@@@@@@@@.........
........@@@@@@@@@@@@@@@@@@@@@@@@@........
.......@@@@@@@@@@@@@@@@@@@@@@@@@@@.......
......@@@@@@@@@@@@@@@@@@@@@@@@@@@@@......
.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.....
....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@....
...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@...
..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..
.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..
...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@...
....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@....
.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.....
......@@@@@@@@@@@@@@@@@@@@@@@@@@@@@......
.......@@@@@@@@@@@@@@@@@@@@@@@@@@@.......
........@@@@@@@@@@@@@@@@@@@@@@@@@........
.........@@@@@@@@@@@@@@@@@@@@@@@.........
..........@@@@@@@@@@@@@@@@@@@@@..........
...........@@@@@@@@@@@@@@@@@@@...........
............@@@@@@@@@@@@@@@@@............
.............@@@@@@@@@@@@@@@.............
..............@@@@@@@@@@@@@..............
...............@@@@@@@@@@@...............
................@@@@@@@@@................
.................@@@@@@@.................
..................@@@@@..................
...................@@@...................
....................@....................
"""

TEST_CASES = [
    (1, DIAMOND_1.strip()),
    (2, DIAMOND_2.strip()),
    (3, DIAMOND_3.strip()),
    (4, DIAMOND_4.strip()),
    (5, DIAMOND_5.strip()),
    (10, DIAMOND_10.strip()),
    (20, DIAMOND_20.strip()),
]

random.seed(0)  # Make all results reproductible

for half_diagonal, diamond in TEST_CASES:
    # Tests with alphanumeric strings
    TestCaseWholeFile(
        test_name=f"Demi-diagonale = {half_diagonal}",
        filename=SOURCE_FILE,
        mock_input=[str(half_diagonal)],
        expected_output=list(map(Equal, diamond.split())),
        timeout=1,
        fail_message="Vérifier votre programme"
    )

    # Tests with invalid inputs
    bad_inputs = ["0.00", "0"]
    should_generate_floats = random.random() < 0.5
    if should_generate_floats:
        bad_inputs += [random.uniform(-20, 20)
                       for _ in range(random.randint(1, 10))]
    should_generate_negative_int = random.random() < 0.5
    if should_generate_negative_int:
        bad_inputs += [random.randint(-20, -1)
                       for _ in range(random.randint(1, 10))]
    should_generate_text = random.random() < 0.5
    if should_generate_text:
        bad_inputs += [random.choice(list("abcdefghijklmnopqrstuvwxyz"))
                       for _ in range(random.randint(1, 10))]

    random.shuffle(bad_inputs)

    bad_inputs = list(map(str, bad_inputs))

    TestCaseWholeFile(
        test_name=f"Demi-diagonale = {half_diagonal} après entrée {bad_inputs}",
        filename=SOURCE_FILE,
        mock_input=bad_inputs + [str(half_diagonal)],
        expected_output=list(map(Equal, diamond.split())),
        timeout=1,
        fail_message="Vérifier votre programme"
    )

if __name__ == "__main__" :
    run_test()