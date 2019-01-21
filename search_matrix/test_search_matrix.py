import unittest

from search_matrix import Solution

class TestSpiralOrder(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        matrix = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 3
        self.assertTrue(solution.searchMatrix(matrix, target))
    
    def test_case2(self):
        solution = Solution()
        matrix = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 13
        self.assertFalse(solution.searchMatrix(matrix, target))


if __name__ == "__main__":
    unittest.main()
