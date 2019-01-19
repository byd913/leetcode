# -*- coding=utf-8 -*-

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1) + 1
        m = len(word2) + 1
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            dp[i][0] = i
        for j in range(m):
            dp[0][j] = j
        
        for i in range(1, n):
            for j in range(1, m):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        
        return dp[n-1][m-1]


if __name__ == "__main__":
    det = [[0 for _ in range(4)] for _ in range(2)]
    print det