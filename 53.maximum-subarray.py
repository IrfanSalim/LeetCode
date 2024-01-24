#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        ans = -float('inf')
        for i in range(len(nums)):
            sum += nums[i]
            ans = max(sum, ans)
            if sum < 0:
                sum = 0
        return ans
# @lc code=end

