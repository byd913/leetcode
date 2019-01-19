# -*- coding=utf-8 -*-
import unittest

from min_distance import Solution

class TestMinDistance(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        word1 = "horse"
        word2 = "ros"
        self.assertEqual(solution.minDistance(word1, word2), 3)
            
    def test_case2(self):
        solution = Solution()
        word1 = "intention"
        word2 = "execution"
        self.assertEqual(solution.minDistance(word1, word2), 5)

    def test_case3(self):
        solution = Solution()
        word1 = ""
        word2 = "exe"
        self.assertEqual(solution.minDistance(word1, word2), 3)

    def test_case4(self):
        solution = Solution()
        word1 = "exe"
        word2 = ""
        self.assertEqual(solution.minDistance(word1, word2), 3)

    def test_case5(self):
        solution = Solution()
        word1 = "exe"
        word2 = "abc"
        self.assertEqual(solution.minDistance(word1, word2), 3)

    def test_case6(self):
        solution = Solution()
        word1 = "exe"
        word2 = "exe"
        self.assertEqual(solution.minDistance(word1, word2), 0)

if __name__ == "__main__":
    unittest.main()
