import unittest

from set_zeros import Solution

class TestSetZeros(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        matrix = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        expect_result = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]
        solution.setZeroes(matrix)
        self.assertListEqual(matrix, expect_result)
    
    def test_case2(self):
        solution = Solution()
        matrix = [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ]
        expect_result = [
            [0, 0, 0, 0],
            [0, 4, 5, 0],
            [0, 3, 1, 0]
        ]
        solution.setZeroes(matrix)
        self.assertListEqual(matrix, expect_result)


if __name__ == "__main__":
    unittest.main()
