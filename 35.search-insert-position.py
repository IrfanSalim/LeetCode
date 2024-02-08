#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        A = nums
        n = len(A)
        l, h = 0, n - 1
        while l <= h:
            mid = l + (h - l)//2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        return l
# @lc code=end

