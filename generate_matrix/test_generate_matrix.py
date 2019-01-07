import unittest

from generate_matrix import Solution

class TestGenerateMatrix(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        n = 1
        expect_result = [[1]]
        result = solution.generateMatrix(n)
        self.assertListEqual(result, expect_result)
    
    def test_case2(self):
        solution = Solution()
        n = 2
        expect_result = [[1,2], [4,3]]
        result = solution.generateMatrix(n)
        self.assertListEqual(result, expect_result)

    def test_case3(self):
        solution = Solution()
        n = 3
        expect_result = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ]
        result = solution.generateMatrix(n)
        self.assertListEqual(result, expect_result)


if __name__ == "__main__":
    unittest.main()