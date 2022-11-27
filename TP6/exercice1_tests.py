import unittest
import numpy as np
from exercice1 import matrix_of_ones, multiplier_matrices, array_max_and_index, array_of_equidistant_points, array_size, top_right_array_elements, third_column, first_row, example_matrix

class Exercice1Tests(unittest.TestCase):
    def test_matrix_of_ones_1(self):
        A = matrix_of_ones(6)
        self.assertEqual(A.shape[0], A.shape[1], msg="La matrice doit être carrée.")
   
    def test_matrix_of_ones_2(self):
        n = 6
        A = matrix_of_ones(n)        
        self.assertEqual(A.shape[0], n, msg="La taille de la matrice n'est pas bonne.")
        self.assertEqual(A.shape[1], n, msg="La taille de la matrice n'est pas bonne.")

    def test_matrix_of_ones_3(self):
        A = matrix_of_ones(4)
        B = np.array([[1, 5, 1, 1],
                      [1, 1, 1, 1],
                      [1, 1, 1, 1],
                      [1, 1, 1, 1]])
        self.assertEqual(A.tolist(), B.tolist(), msg="La matrice retournée par votre fonction n'est pas telle que souhaitée.")

    def test_matrix_of_ones_n_egal_0(self):
        A = matrix_of_ones(0)
        self.assertEqual(A, None, msg="Votre fonction devrait retourner None si n <= 1.")

    def test_matrix_of_ones_n_egal_1(self):
        A = matrix_of_ones(1)
        self.assertEqual(A, None, msg="Votre fonction devrait retourner None si n <= 1.")

    def test_multiplier_matrices_1(self):
        A = np.ones((3, 2))
        B = np.ones((4, 4))
        output = multiplier_matrices(A, B)
        self.assertEqual(output, None)
    
    def test_multiplier_matrices_2(self):
        A = np.ones((3, 2))
        B = np.ones((12, 12))
        output = multiplier_matrices(A, B)
        self.assertEqual(output, None)

    def test_multiplier_matrices_3(self):
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[3, 4], [1, 2]])
        output = multiplier_matrices(A, B)
        self.assertEqual(output, np.array([[5, 8], [13, 20]].tolist()))

    def test_multiplier_matrices_3(self):
        A = np.array([[1, 2, 1], [3, 4, 3], [4, 9, 1]])
        B = np.array([[3, 4, 5], [1, 2, 9], [0, 2, 1]])

        output = multiplier_matrices(A, B)
        expected = np.array([[  5,  10,  24],
                             [ 13,  26,  54],
                             [ 21,  36, 102]])

        self.assertEqual(output.tolist(), expected.tolist())

    def test_array_max_and_index(self):
        array = np.array([10, 9, 8, 144, 0, 1])
        output = array_max_and_index(array)

        self.assertEqual(output, (144, 3))

    def test_array_of_equidistant_points(self):
        output = array_of_equidistant_points()
        expected = np.array([0,  6, 12, 18, 24, 30])
        
        self.assertTrue(np.allclose(output, expected))

    def test_array_size_1(self):
        A = np.array([1])
        self.assertEqual(array_size(A), 1)
    
    def test_array_size_2(self):
        A = np.ones((5, 6))
        self.assertEqual(array_size(A), 5*6)

    def test_top_right_array_elements_1(self):
        A = np.array([[1, 2, 1], 
                      [3, 4, 3], 
                      [4, 9, 1]])
        expected = np.array([[2, 1], [4, 3]])

        self.assertEqual(top_right_array_elements(A).tolist(), expected.tolist())

    def test_top_right_array_elements_2(self):
        A = np.array([[1, 2, 1, 9], 
                      [3, 4, 3, 9], 
                      [4, 9, 1, 10],
                      [1, 4, 5, 0]])
        expected = np.array([[1, 9], [3, 9]])

        self.assertEqual(top_right_array_elements(A).tolist(), expected.tolist())

    def test_top_right_array_elements_3(self):
        A = np.ones((2, 2))
        self.assertEqual(top_right_array_elements(A).tolist(), A.tolist())

    def test_second_column_1(self):
        A = np.array([[1, 2, 1, 9], 
                      [3, 4, 3, 9], 
                      [4, 9, 1, 10],
                      [1, 4, 5, 0]])

        self.assertEqual(third_column(A).tolist(), np.array([1, 3, 1, 5]).tolist())

    def test_second_column_2(self):
        A = np.array([[1, 2, 1],
                      [3, 4, 3], 
                      [4, 9, 1]])

        self.assertEqual(third_column(A).tolist(), np.array([1, 3, 1]).tolist())

    def test_first_row_1(self):
        A = np.array([[1, 2, 1, 9], 
                      [3, 4, 3, 9], 
                      [4, 9, 1, 10],
                      [1, 4, 5, 0]])

        self.assertEqual(first_row(A).tolist(), np.array([1, 2, 1, 9]).tolist())

    def test_first_row_2(self):
        A = np.array([[1, 2, 1],
                      [3, 4, 3], 
                      [4, 9, 1]])

        self.assertEqual(first_row(A).tolist(), np.array([1, 2, 1]).tolist())

    def test_example_matrix(self):
        self.assertEqual(example_matrix().tolist(), [[8, 2, 142, 4],
                     [1, 5, 2, 5],
                     [1, 1, 23, 145]])

if __name__ == '__main__':
    unittest.main(verbosity=2)
