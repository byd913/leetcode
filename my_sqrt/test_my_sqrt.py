# -*- coding=utf-8 -*-
import unittest

from my_sqrt import Solution

class TestIsNumber(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        self.assertEqual(solution.mySqrt(8), 2)
            
    def test_case2(self):
        solution = Solution()
        self.assertEqual(solution.mySqrt(16), 4)


if __name__ == "__main__":
    unittest.main()