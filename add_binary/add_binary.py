# -*- coding=utf-8 -*-

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 and j >= 0:
            ret = int(a[i]) + int(b[j]) + carry
            result.append(str(ret % 2))
            carry = ret / 2
            i -= 1
            j -= 1
        
        while i >= 0:
            ret = int(a[i]) + carry
            result.append(str(ret % 2))
            carry = ret / 2
            i -= 1

        while j >= 0:
            ret = int(b[j]) + carry
            result.append(str(ret % 2))
            carry = ret / 2
            j -= 1
        
        if carry != 0:
            result.append(str(carry))

        return ''.join(result[::-1])


if __name__ == "__main__":
    s = Solution()
    print s.addBinary('1010', '1011')