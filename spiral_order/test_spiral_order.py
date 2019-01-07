import unittest

from spiral_order import Solution

class TestSpiralOrder(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expect_result = [1,2,3,6,9,8,7,4,5]
        result = solution.spiralOrder(matrix)
        self.assertListEqual(result, expect_result)
    
    def test_case2(self):
        solution = Solution()
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        expect_result = [1,2,3,4,8,12,11,10,9,5,6,7]
        result = solution.spiralOrder(matrix)
        self.assertListEqual(result, expect_result)

    def test_case3(self):
        solution = Solution()
        matrix = [[6,9,7]]
        expect_result = [6,9,7]
        result = solution.spiralOrder(matrix)
        self.assertListEqual(result, expect_result)

    def test_case4(self):
        solution = Solution()
        matrix = [[6],[9],[7]]
        expect_result = [6,9,7]
        result = solution.spiralOrder(matrix)
        self.assertListEqual(result, expect_result)

    def test_case5(self):
        solution = Solution()
        matrix = [[1]]
        expect_result = [1]
        result = solution.spiralOrder(matrix)
        self.assertListEqual(result, expect_result)


if __name__ == "__main__":
    unittest.main()