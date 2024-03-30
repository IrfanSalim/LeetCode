#
# @lc app=leetcode id=64 lang=python
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        
        for j in range(1, m):
            grid[j][0] += grid[j-1][0]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[m-1][n-1]

        #------------------------------------------------------------------------------------------------------

        # top down DP approach
        # dp = [[-1] * n for _ in range(m)]

        # def getMin(i, j):
        #     if i < 0 or j < 0:
        #         return float('inf')
        #     if i == 0 and j == 0:
        #         return grid[i][j]
        #     if dp[i][j] == -1:
        #         dp[i][j] = min(getMin(i-1, j), getMin(i, j-1)) + grid[i][j]
        #     return dp[i][j]

        # return getMin(m-1, n-1)
# @lc code=end

