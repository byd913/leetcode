# -*- coding=utf-8 -*-

import unittest
from climb_stairs import Solution

class TestClimbStairs(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        self.assertEqual(solution.climbStairs(2), 2)
            
    def test_case2(self):
        solution = Solution()
        self.assertEqual(solution.climbStairs(3), 3)
    
    def test_case3(self):
        solution = Solution()
        self.assertEqual(solution.climbStairs(4), 5)

if __name__ == "__main__":
    unittest.main()