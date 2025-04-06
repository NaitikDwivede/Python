import unittest
from linear_algebra.matrix_inversion import invert_matrix

class MatrixInversionTest(unittest.TestCase):
    def test_basic_case(self):
        mat = [[4.0, 7.0], [2.0, 6.0]]
        expected_inv = [[0.6, -0.7], [-0.2, 0.4]]
        result = invert_matrix(mat)
        for i in range(2):
            for j in range(2):
                self.assertAlmostEqual(result[i][j], expected_inv[i][j], places=5)

    def test_identity(self):
        mat = [[1.0, 0.0], [0.0, 1.0]]
        self.assertEqual(invert_matrix(mat), mat)

    def test_non_invertible(self):
        mat = [[1.0, 2.0], [2.0, 4.0]]  # determinant zero
        with self.assertRaises(Exception):
            invert_matrix(mat)

if __name__ == "__main__":
    unittest.main()
