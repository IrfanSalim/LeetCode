#
# @lc app=leetcode id=540 lang=python
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]
        l, r = 1, n-2
        while l <= r:
            m = l + (r - l)//2
            if nums[m] != nums[m+1] and nums[m] != nums[m-1]:
                return nums[m]
            if nums[m] == nums[m-1]:
                m -= 1
            if m % 2 == 0:
                l = m + 2
            else:
                r = m - 1
# @lc code=end

