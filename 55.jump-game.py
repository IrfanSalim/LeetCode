#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return True
        end = n-1
        possible = False
        for i in range(n-2, -1, -1):
            if nums[i] >= end - i:
                end = i
                possible = True
            else:
                possible = False
        return possible
            
# @lc code=end

