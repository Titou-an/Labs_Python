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


module = dict()


class TestCaseWholeFile(unittest.TestCase):

    def __init__(self, test_name: str, filename: str, mock_input: List, expected_output: List, timeout: float = None, fail_message: str = None, modeStartsWith: bool = False):
        super(TestCaseWholeFile, self).__init__()
        self.shortDescription = lambda: test_name
        self.file = filename
        self.mock_input = mock_input
        self.expected_output = expected_output
        self.timeout = timeout
        self.fail_message = fail_message
        self.modeStartsWith = modeStartsWith

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

    def run_test_fichier_complet(self):
        @patch('builtins.input', self.override_input())
        def exec():
            try:
                out = StringIO()
                sys.stdout = out
                if self.timeout is not None:
                    timer = threading.Timer(
                        self.timeout, lambda: _thread.interrupt_main())
                    timer.start()
                self.run_whole_file()
                output = out.getvalue().strip().splitlines()

                if(len(output) != len(self.expected_output)):
                    message = f'La sortie de votre programme contient {len(output)} lignes. Vous devez avoir {len(self.expected_output)} lignes'
                    raise Exception(message)

                for result, expected in zip(output, self.expected_output):
                    if self.modeStartsWith:
                        self.assertTrue(result.startswith(expected), msg=f"\n\nVoulu: '{expected}',\nVotre code: '{result}'\nLes décimales exactes ne sont pas importantes.")                
                    else:
                        self.assertEqual(result, expected, self.fail_message)
            except KeyboardInterrupt:
                raise Exception(
                    f'Votre programme n\'a pas terminé son exécution dans le temps alloué de {self.timeout} seconde(s). Vous êtes peut-être dans une boucle infinie.')
            finally:
                sys.stdout = sys.__stdout__
                if self.timeout is not None:
                    timer.cancel()
        exec()

    def runTest(self):
        self.run_test_fichier_complet()


class BasicTestCase(unittest.TestCase):

    def __init__(self, test_name: str, result_func, expected_result, timeout: float, fail_message: str = None):
        super(BasicTestCase, self).__init__()
        self.shortDescription = lambda: test_name
        self.result_func = result_func
        self.expected_result = expected_result
        self.timeout = timeout
        self.fail_message = fail_message

    def runTest(self):
        try:
            if self.timeout is not None:
                timer = threading.Timer(
                    self.timeout, lambda: _thread.interrupt_main())
                timer.start()
            self.assertEqual(self.expected_result,
                             self.result_func(), self.fail_message)
        except KeyboardInterrupt:
            raise Exception(
                f'Votre programme n\'a pas terminé son exécution dans le temps alloué de {self.timeout} seconde(s). Vous êtes peut-être dans une boucle infinie.')
        finally:
            if self.timeout is not None:
                timer.cancel()


class TestSuite:
    def __init__(self):
        self.suite = unittest.TestSuite()

    def add_tests_cases(self, *cases):
        self.suite.addTests(cases)

    def __call__(self):
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(self.suite)