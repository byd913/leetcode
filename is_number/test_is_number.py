# -*- coding=utf-8 -*-
import unittest

from is_number import Solution

class TestIsNumber(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        self.assertTrue(solution.isNumber('-0.11'))
            
    def test_case2(self):
        solution = Solution()
        self.assertFalse(solution.isNumber('--0.11'))

    def test_case3(self):
        solution = Solution()
        self.assertFalse(solution.isNumber('0.1.1'))

    def test_case4(self):
        solution = Solution()
        self.assertTrue(solution.isNumber('123'))

    def test_case5(self):
        solution = Solution()
        self.assertTrue(solution.isNumber('123.5'))

    def test_case6(self):
        solution = Solution()
        self.assertFalse(solution.isNumber('abc'))
    
    def test_case7(self):
        solution = Solution()
        self.assertFalse(solution.isNumber('2.0e10.1'))
    
    def test_case8(self):
        solution = Solution()
        self.assertFalse(solution.isNumber(''))

    def test_case9(self):
        solution = Solution()
        self.assertTrue(solution.isNumber('.1'))

    def test_case10(self):
        solution = Solution()
        self.assertFalse(solution.isNumber('.'))

    def test_case11(self):
        solution = Solution()
        self.assertTrue(solution.isNumber('+.8'))

    def test_case12(self):
        solution = Solution()
        self.assertTrue(solution.isNumber(' 005047e+6'))

    def test_case13(self):
        solution = Solution()
        self.assertFalse(solution.isNumber('e'))

if __name__ == "__main__":
    unittest.main()