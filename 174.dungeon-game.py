#
# @lc app=leetcode id=174 lang=python
#
# [174] Dungeon Game
#

# @lc code=start
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        A = dungeon
        m, n = len(A), len(A[0])

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    A[i][j] = max(1, 1 - A[i][j])
                elif i == m-1:
                    A[i][j] = max(1, A[i][j+1] - A[i][j])
                elif j == n-1:
                    A[i][j] = max(1, A[i+1][j] - A[i][j])
                else:
                    A[i][j] = max(1, min(A[i+1][j], A[i][j+1]) - A[i][j])
        
        return A[0][0]

        #------------------------------------------------------------------------------------------------------

        # DP with top down approach
        # dp = [[-1 for i in range(n)] for j in range(m)]

        # def health(A, i, j):
        #     if i >= m or j >= n:
        #         return float('inf')
        #     if i == m-1 and j == n-1:
        #         return max(1, 1 - A[i][j])
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     dp[i][j] = max(1, min(health(A, i+1, j), health(A, i, j+1)) - A[i][j])
        #     return dp[i][j]
        
        # return health(A, 0, 0)
# @lc code=end

