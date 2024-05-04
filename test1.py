import unittest
from read_data import process_matrix_data
from display import display_matrix_from_data
class TestProcessMatrixData(unittest.TestCase):

    matrix1 = [
                [2, 3, 100],  # Costs to two customers and total provisions for supplier 1
                [4, 1, 150]   # Costs to two customers and total provisions for supplier 2
            ]
    matrix2 = []

    p=process_matrix_data(matrix2)
    display_matrix_from_data(p)

# This allows the tests to be run from the command line
if __name__ == '__main__':
    unittest.main()
