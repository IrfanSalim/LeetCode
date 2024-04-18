#
# @lc app=leetcode id=137 lang=python
#
# [137] Single Number II
#

# @lc code=start
from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        for key in count:
            if count[key] == 1:
                return key
# @lc code=end

