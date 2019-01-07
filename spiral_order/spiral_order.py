
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result_list = []
        height =  len(matrix)
        if height == 0:
            return result_list

        width = len(matrix[0])
        min_w = min(width, height)

        half_w = min_w / 2
        if min_w % 2 == 1:
            half_w += 1

        for k in range(0, half_w):
            start_w = k
            end_w = width-1-k
            start_h = k
            end_h = height-1-k

            i = start_h
            for j in range(start_w, end_w):
                result_list.append(matrix[i][j])
            
            j = end_w
            for i in range(start_h, end_h):
                result_list.append(matrix[i][j])
            
            i = end_h
            if end_h > start_h:
                for  j in range(end_w, start_w, -1):
                    result_list.append(matrix[i][j])
            else:
                result_list.append(matrix[i][end_w])
            
            j = start_w
            if end_w > start_w:
                for i in range(end_h, start_h, -1):
                    result_list.append(matrix[i][j])
            elif end_h > start_h:
                result_list.append(matrix[end_h][j])
        
        return result_list




if __name__ == "__main__":
    matrix = [[1]]
    solution = Solution()
    print solution.spiralOrder(matrix)
