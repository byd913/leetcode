class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial_list = [0] * (n + 1)

        m = 1
        for i in range(1, n+1):
            factorial_list[i] = m
            m *= i+1
        
        ret_str = ''
        exist_set = set()
        k = k-1
        for i in range(n-1, 0, -1):
            factor = int(k / factorial_list[i])

            less_count = 0
            for j in range(1, n+1):
                if j in exist_set:
                    continue
                if less_count == factor:
                    ret_str += str(j)
                    exist_set.add(j)
                    break
                less_count += 1

            k = k % factorial_list[i]
        for i in range(1, n+1):
            if i not in exist_set:
                ret_str += str(i)
        return ret_str

    
if __name__ == "__main__":
    s = Solution()
    print s.getPermutation(9, 2)