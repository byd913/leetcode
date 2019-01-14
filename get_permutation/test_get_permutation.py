import unittest

from get_permutation import Solution

class TestGetPermutation(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        n = 1
        k = 1
        expect_result = '1'
        result = solution.getPermutation(n, k)
        self.assertEqual(result, expect_result)
    
    def test_case2(self):
        solution = Solution()
        n = 2
        k = 1
        expect_result = '12'
        result = solution.getPermutation(n, k)
        self.assertEqual(result, expect_result)

    def test_case3(self):
        solution = Solution()
        n = 3
        k = 6
        expect_result = '321'
        result = solution.getPermutation(n, k)
        self.assertEqual(result, expect_result)

    def test_case4(self):
        solution = Solution()
        n = 3
        k = 3
        expect_result = '213'
        result = solution.getPermutation(n, k)
        self.assertEqual(result, expect_result)


if __name__ == "__main__":
    unittest.main()