#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for n in nums:
            ans = ans ^ n
        return ans
# @lc code=end

