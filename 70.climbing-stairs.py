#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev, curr = 0, 1
        for i in range(n):
            next = prev + curr
            prev = curr
            curr = next
        return curr


        #using top down DP, or tabulation
        # if n <= 2:
        #     return n
        
        # dp = [1, 2]
        
        # for i in range(2, n):
        #     curr = dp[i-1] + dp[i-2]
        #     dp.append(curr)
        
        # return dp[-1]


        # using DP bottom-up
        # dp = [-1] * (n+1)

        # def rec(A):
        #     if A <= 2:
        #         return A
            
        #     if dp[A] != -1:
        #         return dp[A]
            
        #     dp[A] = rec(A-1) + rec(A-2)
        #     return dp[A]
        
        # return rec(n)


        #using basic recursion
        # def rec(A):
        #     if A <= 2:
        #         return A
        #     return rec(A - 1) + rec(A-2)

        # return rec(n)
        
# @lc code=end

