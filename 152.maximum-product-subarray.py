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
        # maxSoFar = nums[0]
        # minSoFar = nums[0]
        # maxProduct = nums[0]
        # for i in range(1, len(nums)):
        #     curr = nums[i]
        #     tempMax = max(curr, curr * maxSoFar, curr * minSoFar)
        #     minSoFar = min(curr, curr * maxSoFar, curr * minSoFar)
        #     maxSoFar = tempMax
        #     maxProduct = max(maxProduct, maxSoFar)
        # return maxProduct

        #------------------------------------------------------------------------------------------------------

        # second approach with traversing forward and backward to get max
        ans = max(nums)
        product = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                product = 1
                continue
            product *= nums[i]
            ans = max(ans, product)

        product = 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                product = 1
                continue
            product *= nums[i]
            ans = max(ans, product)
        
        return ans

# @lc code=end
    

