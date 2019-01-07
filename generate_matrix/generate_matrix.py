
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = []
        for i in range(0, n):
            matrix.append([0] * n)

        half_n = n / 2
        if n % 2 == 1:
            half_n += 1

        number = 1
        for k in range(0, half_n):
            s = k
            e = n-1-k

            i = s
            for j in range(s, e):
                matrix[i][j] = number
                number += 1
            
            j = e
            for i in range(s, e):
                matrix[i][j] = number
                number += 1
            
            i = e
            if e > s:
                for  j in range(e, s, -1):
                    matrix[i][j] = number
                    number += 1
            else:
                j = e
                matrix[i][j] = number
                number += 1
            
            j = s
            if e > s:
                for i in range(e, s, -1):
                    matrix[i][j] = number
                    number += 1
        
        return matrix


if __name__ == "__main__":
    solution = Solution()
    print solution.generateMatrix(3)