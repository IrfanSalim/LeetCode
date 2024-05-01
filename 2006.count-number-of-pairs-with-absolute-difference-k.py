#
# @lc app=leetcode id=2006 lang=python
#
# [2006] Count Number of Pairs With Absolute Difference K
#

# @lc code=start
class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        freq = {}
        ans = 0
        for i in range(n):
            x = nums[i]
            y = x - k
            z = k + x
            if y in freq:
                ans += freq[y]
            if z in freq:
                ans += freq[z]
            freq[x] = freq.get(x, 0) + 1
        return ans
# @lc code=end

