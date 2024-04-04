#
# @lc app=leetcode id=45 lang=python
#
# [45] Jump Game II
#

# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # bottom up DP approach
        n = len(nums)
        dp = [0] * (n+1)
        dp[0] = 0

        for i in range(1, n):
            minVal = float('inf')
            for j in range(i-1, -1, -1):
                if j + nums[j] >= i:
                    minVal = min(minVal, dp[j])
            dp[i] = minVal + 1
        
        return dp[n-1]
# @lc code=end

