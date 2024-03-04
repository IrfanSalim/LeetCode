#
# @lc app=leetcode id=219 lang=python
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen and abs(seen[nums[i]] - i) <= k:
                return True
            else:
                seen[nums[i]] = i
        return False
# @lc code=end

