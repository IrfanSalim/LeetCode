#
# @lc app=leetcode id=96 lang=python
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # bottom up faster approach
        dp = [1] * (n+1)

        for nodes in range(2, n+1):
            total = 0
            for root in range(1, nodes+1):
                left = root - 1
                right = nodes - root
                total += dp[left] * dp[right]
            dp[nodes] = total
        
        return dp[n]

        # top down dp approach
        # dp = [-1] * (n+1)

        # def totalTrees(i):
        #     if i <= 1:
        #         return 1
        #     if dp[i] == -1:
        #         total = 0
        #         for j in range(1, i+1):
        #             left = totalTrees(j-1,)
        #             right = totalTrees(i-j)
        #             total += left * right
        #         dp[i] = total
        #     return dp[i]
        
        # return totalTrees(n)
# @lc code=end

