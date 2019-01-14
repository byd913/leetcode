class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        step_matrix = []
        for i in range(0, height):
            step_matrix.append([0] * width)

        if obstacleGrid[0][0] != 0:
            return 0
        
        step_matrix[0][0] = 1
        for i in range(0, height):
            for j in range(0, width):
                if obstacleGrid[i][j] != 0:
                    step_matrix[i][j] = 0
                    continue

                if i > 0:
                    step_matrix[i][j] = step_matrix[i-1][j]
                if j > 0:
                    step_matrix[i][j] += step_matrix[i][j-1]

        return step_matrix[height-1][width-1]