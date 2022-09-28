__author__ = "Marc-Olivier Derouin"

import threading
import _thread
import unittest
from unittest.mock import patch
from typing import List
from io import StringIO
from collections import deque
import sys
import importlib
import re

class Equal:
    def __init__(self, expected):
        self.expected = expected

    def validate(self, unittest, value_to_test, fail_message: str):
        unittest.assertEqual(value_to_test, self.expected, fail_message)

class AlmostEqualNumber:
    def __init__(self, expected: str, precisions: List):
        self.expected = expected
        self.precisions = precisions

    def validate(self, unittest, value_to_test, fail_message):
        regex_pattern = r"[-+]?(?:\d*\.\d+|\d+)"
        expected_numbers = re.findall(regex_pattern, self.expected)

        if len(self.precisions) != len(expected_numbers):
            raise Exception("Precision manquante dans la definition du test.")

        result_numbers = re.findall(regex_pattern, value_to_test)

        if len(expected_numbers) != len(result_numbers):
            message = f'La sortie de votre programme contient {len(result_numbers)} float. Vous devez avoir {len(expected_numbers)} float'
            raise Exception(message)

        for expected_number, result_number, precision in zip(expected_numbers, result_numbers, self.precisions):
            try:
                unittest.assertAlmostEqual(float(expected_number), float(result_number), precision, fail_message)
            except ValueError:
                raise Exception("Impossible de convertir en float")



def timeout(timeout_time):
    def decorator(function):
        def inner(*args, **kwargs):
            try:
                if timeout_time is not None:
                    timer = threading.Timer(timeout_time, lambda: _thread.interrupt_main())
                    timer.start()
                function(*args, **kwargs)
            except KeyboardInterrupt:
                raise Exception(
                    f'Votre programme n\'a pas terminé son exécution dans le temps alloué de {timeout_time} seconde(s). Vous êtes peut-être dans une boucle infinie.')
            finally:
                if timeout_time is not None:
                    timer.cancel()
        return inner
    return decorator

module = dict()

class TestCaseWholeFile(unittest.TestCase):
    tests_case = []
    def __init__(self, test_name: str, filename: str, mock_input: List, expected_output: List, timeout: float = None, fail_message: str = None):
        super(TestCaseWholeFile, self).__init__()
        self.shortDescription = lambda: test_name
        self.file = filename
        self.mock_input = mock_input
        self.expected_output = expected_output
        self.timeout = timeout
        self.fail_message = fail_message
        TestCaseWholeFile.tests_case.append(self)

    def run_whole_file(self):
        if self.file not in module:
            module[self.file] = importlib.import_module(self.file)
        else:
            importlib.reload(module[self.file])

    def override_input(self):
        queue = deque(self.mock_input)
        def fake_input(*args):
            if len(queue) == 0:
                raise Exception(
                    "Vous avez appelé input trop souvent. Vérifiez votre code")
            return queue.popleft()
        return fake_input

    def runTest(self):
        @patch('builtins.input', self.override_input())
        @timeout(self.timeout)
        def exec():
            try:
                out = StringIO()
                sys.stdout = out
                self.run_whole_file()
                output = out.getvalue().strip().splitlines()

                if(len(output) != len(self.expected_output)):
                    message = f'La sortie de votre programme contient {len(output)} lignes. Vous devez avoir {len(self.expected_output)} lignes'
                    raise Exception(message)
                for result, expected in zip(output, self.expected_output):
                    expected.validate(self, result, self.fail_message)
            finally:
                sys.stdout = sys.__stdout__
        exec()


class BasicTestCase(unittest.TestCase):
    tests_case = []
    def __init__(self, test_name: str, result_func, expected_result, timeout: float, fail_message: str = None):
        super(BasicTestCase, self).__init__()
        self.shortDescription = lambda: test_name
        self.result_func = result_func
        self.expected_result = expected_result
        self.timeout = timeout
        self.fail_message = fail_message
        BasicTestCase.tests_case.append(self)

    def runTest(self):
        @timeout(self.timeout)
        def run():
            self.assertEqual(self.expected_result, self.result_func(), self.fail_message)
        run()


def run_test():
    suite = unittest.TestSuite()
    suite.addTests(BasicTestCase.tests_case)
    suite.addTests(TestCaseWholeFile.tests_case)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
