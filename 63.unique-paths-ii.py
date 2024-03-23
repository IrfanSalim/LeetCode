#
# @lc app=leetcode id=63 lang=python
#
# [63] Unique Paths II
#

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        A = obstacleGrid
        n = len(A[0])
        m = len(A)
        if A[m-1][n-1] or A[0][0] == 1:
            return 0
        A[0][0] = 1
        for i in range(1, m):
            if A[i][0] == 1:
                A[i][0] = -1
                continue
            A[i][0] = A[i-1][0]
        
        for i in range(1, n):
            if A[0][i] == 1:
                A[0][i] = -1
                continue
            A[0][i] = A[0][i-1]
        
        for i in range(1, m):
            for j in range(1, n):
                if A[i][j] == 1:
                    A[i][j] = -1
        
        for i in range(1, m):
            for j in range(1, n):
                if A[i][j] == -1:
                    continue
                up = A[i-1][j] if A[i-1][j] != -1 else 0
                left = A[i][j-1] if A[i][j-1] != -1 else 0
                A[i][j] = up + left
        print(A)
        return A[m-1][n-1]

        #------------------------------------------------------------------------------------------------------

        # dp approach top down
        # dp = [[-1] * n for _ in range(m)]
        # def paths(A, i, j):
        #     if i < 0 or j < 0:
        #         return 0
        #     if A[i][j] == 1:
        #         return 0
        #     if i == 0 and j == 0:
        #         return 1
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     dp[i][j] = paths(A, i-1, j) + paths(A, i, j-1)
        #     return dp[i][j]
        # return paths(A, m-1, n-1)
        
# @lc code=end

