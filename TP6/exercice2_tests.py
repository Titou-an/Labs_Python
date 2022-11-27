import unittest
from exercice2 import *

class Exercice2Tests(unittest.TestCase):
    def test_incidents_par_ligne(self):
        self.assertDictEqual(incidents_par_ligne(), {'orange': 424, 'verte': 452, 'jaune': 56, 'bleue': 124}, msg="Votre nombre d'incidents par ligne n'est pas exact.")
    
    def test_incidents_par_mois(self):
        self.assertListEqual(incidents_par_mois(), [101, 75, 80, 90, 66, 84, 81, 64, 76, 98, 120, 93], msg="Votre nombre d'incidents par mois n'est pas exact.")

if __name__ == '__main__':
    unittest.main(verbosity=2)