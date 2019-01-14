class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        total_step = m + n - 2

        if total_step == 0:
            return 1
        
        min_s = min(m-1, n-1)

        molecule = 1
        denominator = 1
        for i in range(min_s):
            molecule *= total_step
            denominator *= min_s
            total_step -= 1
            min_s -= 1
        
        return molecule / denominator