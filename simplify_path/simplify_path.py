# -*- coding=utf-8 -*-


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        result_list = []
        items = path.split('/')
        for item in items:
            if len(item) == 0:
                continue
            elif item == '.':
                continue
            elif item == '..':
                if len(result_list) > 0:
                    result_list = result_list[:-1]
            else:
                result_list.append(item)
        return '/' + '/'.join(result_list)