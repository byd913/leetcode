import unittest

from sort_color import Solution

class TestSortColor(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        nums = [2, 0, 2, 1, 1, 0]
        expect_result = [0, 0, 1, 1, 2, 2]
        solution.sortColors(nums=nums)
        self.assertListEqual(nums, expect_result)
    

if __name__ == "__main__":
    unittest.main()
