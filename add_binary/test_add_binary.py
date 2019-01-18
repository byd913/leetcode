        
import unittest

from add_binary import Solution

class TestAddBinary(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        expect_result = '100'
        result = solution.addBinary('11', '1')
        self.assertEqual(result, expect_result)
    
    def test_case2(self):
        solution = Solution()
        expect_result = '10101'
        result = solution.addBinary('1010', '1011')
        self.assertEqual(result, expect_result)


if __name__ == "__main__":
    unittest.main()
