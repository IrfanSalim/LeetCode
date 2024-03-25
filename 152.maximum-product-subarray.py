#
# @lc app=leetcode id=152 lang=python
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSoFar = nums[0]
        minSoFar = nums[0]
        maxProduct = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            tempMax = max(curr, curr * maxSoFar, curr * minSoFar)
            minSoFar = min(curr, curr * maxSoFar, curr * minSoFar)
            maxSoFar = tempMax
            maxProduct = max(maxProduct, maxSoFar)
        return maxProduct
# @lc code=end
    

