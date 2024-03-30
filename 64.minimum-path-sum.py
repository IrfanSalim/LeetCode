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
        dp = [[-1] * n for _ in range(m)]

        def getMin(i, j):
            if i < 0 or j < 0:
                return float('inf')
            if i == 0 and j == 0:
                return grid[i][j]
            if dp[i][j] == -1:
                dp[i][j] = min(getMin(i-1, j), getMin(i, j-1)) + grid[i][j]
            return dp[i][j]

        return getMin(m-1, n-1)
# @lc code=end

