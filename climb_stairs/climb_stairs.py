# -*- coding=utf-8 -*-


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2

        fn2 = 1
        fn1 = 2
        for i in range(2, n):
            fn = fn1 + fn2
            fn2 = fn1
            fn1 = fn
        return fn