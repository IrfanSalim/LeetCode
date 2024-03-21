#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[-1 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

        #------------------------------------------------------------------------------------------------------

        # DP with top down approach
        # def ways(i, j):
        #     if i == 0 or j == 0:
        #         return 1
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     dp[i][j] = ways(i-1, j) + ways(i, j-1)
        #     return dp[i][j]
        
        # return ways(m-1, n-1)
# @lc code=end

