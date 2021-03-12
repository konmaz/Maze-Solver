import unittest
from src import Maze as mz
import numpy as np


class MyTestCase(unittest.TestCase):

    def testValidStates(self):  # test extreme cases function
        A = np.array([[0, 0, 0, 1, 1, 1, 0, 0, 1, 1],
                      [0, 1, 0, 0, 1, 2, 0, 0, 0, 0],
                      [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 1, 1, 0, 0, 0, 0, 3],
                      [0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
                      [0, 1, 0, 0, 0, 1, 0, 0, 0, 0]])

        self.assertEqual(mz.getValidStates(A, (3, 1)), [(3, 0), (3, 2)])
        self.assertEqual(mz.getValidStates(A, (5, 9)), [(5, 8)])
        self.assertEqual(mz.getValidStates(A, (0, 0)), [(0, 1), (1, 0)])
        self.assertEqual(mz.getValidStates(A, (5, 0)), [(4, 0)])
        self.assertEqual(mz.getValidStates(A, (0, 9)), [(1, 9)])
        self.assertEqual(mz.getValidStates(A, (2, 5)), [(2, 4), (1, 5), (2, 6), (3, 5)])
        self.assertEqual(mz.getValidStates(A, (1, 5)), [(1, 6), (2, 5)])

if __name__ == '__main__':
    unittest.main()
