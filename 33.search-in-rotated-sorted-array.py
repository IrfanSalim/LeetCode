#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        A = nums
        n = len(A)
        l, h = 0, n-1
        while l <= h:
            m = l + (h - l)//2
            if A[m] == target:
                return m
            elif A[l] <= A[m]:
                if target < A[m] and target >= A[l]:
                    h = m - 1
                else:
                    l = m + 1
            else:
                if target > A[m] and target <= A[h]:
                    l = m + 1
                else:
                    h = m - 1
        return -1
# @lc code=end

