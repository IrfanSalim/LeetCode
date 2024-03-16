#
# @lc app=leetcode id=279 lang=python
#
# [279] Perfect Squares
#

# @lc code=start
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # recursive top-down approach
        dp = [-1] * (n+1)
        def minSquares(A):
            if A <= 3:
                return A
            if dp[A] != -1:
                return dp[A]
            x = 1
            ans = A
            while x*x <= A:
                ans = min(ans, minSquares(A - (x*x)))
                x += 1
            dp[A] = ans + 1
            return dp[A]
        return minSquares(n)
        
# @lc code=end

