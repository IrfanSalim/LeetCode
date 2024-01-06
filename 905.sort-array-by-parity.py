#
# @lc app=leetcode id=905 lang=python
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums
        p1, p2 = 0, 0
        while p2 < len(nums) and p1 < len(nums):
            if nums[p2] % 2 == 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 += 1
                p1 += 1
            else:
                p2 += 1
        return nums
# @lc code=end

