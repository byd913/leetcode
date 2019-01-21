# -*- coding=utf-8 -*-

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        height = len(matrix)
        if height == 0:
            return False

        width = len(matrix[0])

        left = 0
        right = width * height - 1
        while left <= right:
            middle = (left + right) // 2
            i = middle / width
            j = middle % width

            if matrix[i][j] < target:
                left = middle + 1
            elif matrix[i][j] > target:
                right = middle - 1
            else:
                return True
            
        return False


if __name__ == "__main__":
    solution = Solution()
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    solution.searchMatrix(matrix=matrix, target=12)