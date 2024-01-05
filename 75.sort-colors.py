#
# @lc app=leetcode id=75 lang=python
#
# [75] Sort Colors
#

# @lc code=start
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, len(nums) - 1
        A = nums
        while i <= k:
            if A[i] == 0:
                A[j], A[i] = A[i], A[j]
                i += 1
                j += 1
            elif A[i] == 2:
                A[i], A[k] = A[k], A[i]
                k -= 1
            else:
                i += 1
        return A

# @lc code=end

