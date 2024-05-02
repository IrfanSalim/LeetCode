#
# @lc app=leetcode id=1143 lang=python
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # bottom up dp approach
        m = len(text1)
        n = len(text2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]

        # top down DP approach
        # m = len(text1)
        # n = len(text2)
        # dp = [[-1 for i in range(n+1)] for j in range(m+1)]

        # def helper(i, j):
        #     if i == 0 or j == 0:
        #         return 0
        #     if dp[i][j] == -1:
        #         if text1[i-1] == text2[j-1]:
        #             dp[i][j] = helper(i - 1, j - 1) + 1
        #         else:
        #             dp[i][j] = max(helper(i-1, j), helper(i, j-1))
        #     return dp[i][j]

        # return helper(m, n)
# @lc code=end

