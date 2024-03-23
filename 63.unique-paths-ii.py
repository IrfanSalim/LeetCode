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
        dp = [[-1] * n for _ in range(m)]
        def paths(A, i, j):
            if i < 0 or j < 0:
                return 0
            if A[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = paths(A, i-1, j) + paths(A, i, j-1)
            return dp[i][j]
        return paths(A, m-1, n-1)
        
# @lc code=end

