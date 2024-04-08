#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != curr:
                if count == 0:
                    curr = nums[i]
                    count = 1
                else:
                    count -= 1
            else:
                count += 1
        return curr
# @lc code=end

