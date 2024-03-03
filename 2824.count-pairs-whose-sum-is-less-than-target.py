#
# @lc app=leetcode id=2824 lang=python
#
# [2824] Count Pairs Whose Sum is Less than Target
#

# @lc code=start
class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i, j = 0, len(nums) - 1
        ans = 0
        while i < j:
            if nums[i] + nums[j] < target:
                ans += j - i
                i += 1
            else:
                j -= 1
        return ans
# @lc code=end

