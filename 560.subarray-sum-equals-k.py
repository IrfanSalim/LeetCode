#
# @lc app=leetcode id=560 lang=python
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        summ = 0
        seen = {0: 1}
        count = 0
        for i in range(len(nums)):
            summ += nums[i]
            x = summ
            y = x - k
            if y in seen:
                count += seen[y]
            elif x == k:
                count += 1
            seen[x] = seen.get(x, 0) + 1
        return count
# @lc code=end

