#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        odd, eve = 0, 0
        for i in range(len(nums)):
            temp = max(odd + nums[i], eve)
            odd = eve
            eve = temp
        return eve

        # dp solution with recursion
        # dp = [-1] * (len(nums) + 1)

        # def getMax(i, A):
        #     if i >= len(A):
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
        #     dp[i] = max(A[i] + getMax(i+2, A), getMax(i+1, A))
        #     return dp[i]
        
        # return getMax(0, nums)
# @lc code=end

