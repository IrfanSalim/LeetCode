#
# @lc app=leetcode id=120 lang=python
#
# [120] Triangle
#

# @lc code=start
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        n = len(triangle[m-1])
        for i in range(m-2, -1, -1):
            for j in range(len(triangle[i])):
                carry = min(triangle[i+1][j], triangle[i+1][j+1])
                triangle[i][j] += carry
        return triangle[0][0]

        # DP top down approach
        # dp = [[-1] * n for _ in range(m)]

        # def minSum(i, j):
        #     if i > m or j > n:
        #         return 0
        #     if i == m-1:
        #         return triangle[i][j]
        #     if dp[i][j] == -1:
        #         dp[i][j] = min(minSum(i+1, j), minSum(i+1, j+1)) + triangle[i][j]
        #     return dp[i][j]

        # return minSum(0, 0)
        
# @lc code=end

