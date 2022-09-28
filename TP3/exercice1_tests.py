import random
from utils_ne_pas_supprimer import TestCaseWholeFile, run_test, Equal

SOURCE_FILE = "exercice1"
FIBONACCI_SEQUENCE = [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    6765,
    10946,
    17711,
    28657,
    46368,
    75025,
    121393,
    196418,
    317811,
    514229,
    832040,
    1346269,
    2178309,
    3524578,
    5702887,
    9227465,
    14930352,
    24157817,
    39088169,
    63245986,
    102334155,
    165580141,
    267914296,
    433494437,
    701408733,
    1134903170,
    1836311903,
    2971215073,
    4807526976,
    7778742049,
    12586269025,
    20365011074,
    32951280099,
    53316291173,
    86267571272,
    139583862445,
    225851433717,
    365435296162,
    591286729879,
    956722026041,
    1548008755920,
    2504730781961,
    4052739537881,
    6557470319842,
    10610209857723,
    17167680177565,
    27777890035288,
    44945570212853,
    72723460248141,
    117669030460994,
    190392490709135,
    308061521170129,
    498454011879264,
    806515533049393,
    1304969544928657,
    2111485077978050,
    3416454622906707,
    5527939700884757,
    8944394323791464,
    14472334024676221,
    23416728348467685,
    37889062373143906,
    61305790721611591,
    99194853094755497,
    160500643816367088,
    259695496911122585,
    420196140727489673,
    679891637638612258,
    1100087778366101931,
    1779979416004714189,
    2880067194370816120,
    4660046610375530309,
    7540113804746346429,
    12200160415121876738,
    19740274219868223167,
    31940434634990099905,
    51680708854858323072,
    83621143489848422977,
    135301852344706746049,
    218922995834555169026,
]

random.seed(0)  # Make all results reproductible

for n in range(1, len(FIBONACCI_SEQUENCE) + 1):
    # Tests with alphanumeric strings
    expected_output = [
        Equal(
            f"La serie recherchee est : {' '.join(str(FIBONACCI_SEQUENCE[i]) for i in range(n))}")
    ]
    fail_message = "Vérifier votre programme"

    TestCaseWholeFile(
        test_name=f"n = {n}",
        filename=SOURCE_FILE,
        mock_input=[str(n)],
        expected_output=expected_output,
        timeout=1,
        fail_message=fail_message
    )

    # Tests with invalid inputs
    invalid_inputs = ["0.00", "0"]
    should_generate_floats = random.random() < 0.5
    if should_generate_floats:
        invalid_inputs += [random.uniform(-20, 20)
                           for _ in range(random.randint(1, 10))]
    should_generate_negative_int = random.random() < 0.5
    if should_generate_negative_int:
        invalid_inputs += [random.randint(-20, -1)
                           for _ in range(random.randint(1, 10))]
    should_generate_text = random.random() < 0.5
    if should_generate_text:
        invalid_inputs += [random.choice(list("abcdefghijklmnopqrstuvwxyz"))
                           for _ in range(random.randint(1, 10))]
    invalid_inputs = list(map(str, invalid_inputs))

    random.shuffle(invalid_inputs)

    TestCaseWholeFile(
        test_name=f"n = {n} apres entrees invalides : {invalid_inputs}",
        filename=SOURCE_FILE,
        mock_input=invalid_inputs + [str(n)],
        expected_output=expected_output,
        timeout=1,
        fail_message="Vérifier votre programme"
    )

if __name__ == "__main__" :
    run_test()
