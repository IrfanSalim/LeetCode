#
# @lc app=leetcode id=1004 lang=python
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i, j = 0, 0
        ans = 0
        count = 0
        while j < len(nums):
            if nums[j] == 0:
                count += 1
                while count > k:
                    if nums[i] == 0:
                        count -= 1
                    i += 1
            if j - i + 1 > ans:
                ans = j - i + 1
            j += 1
        return ans
        
# @lc code=end

