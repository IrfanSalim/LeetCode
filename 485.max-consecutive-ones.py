#
# @lc app=leetcode id=485 lang=python
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        ans = 0
        count = 0
        while j < len(nums):
            if nums[j] == 0:
                ans = max(count, ans)
                count = 0
                j += 1
            else:
                count += 1
                j += 1
        return max(count, ans)

# @lc code=end

