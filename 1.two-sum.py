#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        comp = {}
        for i in range(len(nums)):
            if nums[i] in comp:
                return [comp[nums[i]], i]
            else:
                comp[target - nums[i]] = i
        
# @lc code=end

