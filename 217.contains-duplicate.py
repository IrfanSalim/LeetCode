#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dup = set([])
        for ele in nums:
            if ele in dup:
                return True
            else:
                dup.add(ele)
        return False
# @lc code=end

