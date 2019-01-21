# -*- coding=utf-8 -*-

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red_cnt = 0
        white_cnt = 0
        blue_cnt = 0

        for num in nums:
            if num == 0:
                red_cnt += 1
            elif num == 1:
                white_cnt += 1
            elif num == 2:
                blue_cnt += 1
        
        for i in range(red_cnt):
            nums[i] = 0
        for i in range(red_cnt, red_cnt + white_cnt):
            nums[i] = 1
        for i in range(red_cnt + white_cnt, red_cnt + white_cnt + blue_cnt):
            nums[i] = 2 