import unittest

from unique_path import Solution

class TestUniquePath(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        expect_result = 3
        result = solution.uniquePaths(m=3, n=2)
        self.assertEqual(result, expect_result)
    
    def test_case2(self):
        solution = Solution()
        expect_result = 28
        result = solution.uniquePaths(m=7, n=3)
        self.assertEqual(result, expect_result)

    def test_case3(self):
        solution = Solution()
        expect_result = 1
        result = solution.uniquePaths(m=7, n=1)
        self.assertEqual(result, expect_result)

    def test_case4(self):
        solution = Solution()
        expect_result = 0
        result = solution.uniquePaths(m=1, n=1)
        self.assertEqual(result, expect_result)


if __name__ == "__main__":
    unittest.main()
