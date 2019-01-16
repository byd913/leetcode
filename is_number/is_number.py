# -*- coding=utf-8 -*-

class Solution(object):
    def remove_sign(self, s):
        if len(s) == 0:
            return s

        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        return s

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if len(s) == 0:
            return False

        exp_items = s.split('e')
        if len(exp_items) > 2:
            return False
        
        exp_items[0] = self.remove_sign(exp_items[0])
        items = exp_items[0].split('.')
        if len(items) > 2:
            return False
        
        has_digit = False
        for item in items:
            if len(item) != 0 and not item.isdigit():
                return False
            if item.isdigit():
                has_digit = True
        if not has_digit:
            return False
        
        if len(exp_items) == 2:
            exp_items[1] = self.remove_sign(exp_items[1])
            if not  exp_items[1].isdigit():
                return False
        
        return True


if __name__ == "__main__":
    print ''.isdigit()