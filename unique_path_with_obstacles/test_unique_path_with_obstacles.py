# -*- coding=utf-8 -*-
import unittest

from unique_path_with_obstacles import Solution

class TestUniquePath(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        obstacle_grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        expect_result = 2
        result = solution.uniquePathsWithObstacles(obstacle_grid)
        self.assertEqual(result, expect_result)
    
    def test_case2(self):
        solution = Solution()
        obstacle_grid = [[0]]
        expect_result = 1
        result = solution.uniquePathsWithObstacles(obstacle_grid)
        self.assertEqual(result, expect_result) 

    def test_case3(self):
        solution = Solution()
        obstacle_grid = [
            [0],
            [1],
            [0]
        ]
        expect_result = 0
        result = solution.uniquePathsWithObstacles(obstacle_grid)
        self.assertEqual(result, expect_result)

    def test_case4(self):
        solution = Solution()
        obstacle_grid = [
            [0, 1, 0]
        ]
        expect_result = 0
        result = solution.uniquePathsWithObstacles(obstacle_grid)
        self.assertEqual(result, expect_result)

    def test_case5(self):
        solution = Solution()
        obstacle_grid = [[1]]
        expect_result = 0
        result = solution.uniquePathsWithObstacles(obstacle_grid)
        self.assertEqual(result, expect_result) 

    def test_case6(self):
        solution = Solution()
        obstacle_grid = [[1, 0]]
        expect_result = 0
        result = solution.uniquePathsWithObstacles(obstacle_grid)
        self.assertEqual(result, expect_result) 


if __name__ == "__main__":
    unittest.main()

