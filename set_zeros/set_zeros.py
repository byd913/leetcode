# -*- coding=utf-8 -*-

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return matrix

        height = len(matrix)
        width = len(matrix[0])

        row_zero_index_list = []
        col_zero_index_list = []

        for i in range(0, height):
            for j in range(0, width):
                if matrix[i][j] == 0:
                    row_zero_index_list.append(i)
                    break
        for j in range(0, width):
            for i in range(0, height):
                if matrix[i][j] == 0:
                    col_zero_index_list.append(j)
        
        for idx in row_zero_index_list:
            for j in range(0, width):
                matrix[idx][j] = 0
        for idx in col_zero_index_list:
            for i in range(0, height):
                matrix[i][idx] = 0