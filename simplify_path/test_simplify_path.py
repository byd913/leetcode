# -*- coding=utf-8 -*-
import unittest

from simplify_path import Solution

class TestIsNumber(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        input_path = '/home/'
        expect_result = '/home'
        self.assertEqual(solution.simplifyPath(input_path), expect_result)
            
    def test_case2(self):
        solution = Solution()
        input_path = '/../'
        expect_result = '/'
        self.assertEqual(solution.simplifyPath(input_path), expect_result)

    def test_case3(self):
        solution = Solution()
        input_path = '/home//foo'
        expect_result = '/home/foo'
        self.assertEqual(solution.simplifyPath(input_path), expect_result)
        
    def test_case4(self):
        solution = Solution()
        input_path = '/a/./b/../../c/'
        expect_result = '/c'
        self.assertEqual(solution.simplifyPath(input_path), expect_result)

    def test_case5(self):
        solution = Solution()
        input_path = '/a/../../b/../c//.//'
        expect_result = '/c'
        self.assertEqual(solution.simplifyPath(input_path), expect_result)

    def test_case6(self):
        solution = Solution()
        input_path = '/a//b////c/d//././/..'
        expect_result = '/a/b/c'
        self.assertEqual(solution.simplifyPath(input_path), expect_result)


if __name__ == "__main__":
    unittest.main()