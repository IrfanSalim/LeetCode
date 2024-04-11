#
# @lc app=leetcode id=31 lang=python
#
# [31] Next Permutation
#

# @lc code=start
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1

        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return
        
        i -= 1
        
        j = n-1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        
        nums[i], nums[j] = nums[j], nums[i]

        i, j = i+1, n-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]   
            i += 1
            j -= 1     
# @lc code=end

