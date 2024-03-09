#
# @lc app=leetcode id=162 lang=python
#
# [162] Find Peak Element
#

# @lc code=start
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = nums
        n = len(A)
        if n == 1:
            return 0
        if A[0] > A[1]:
            return 0
        if A[n-1] >= A[n-2]:
            return n-1
        l, r = 1, n - 2
        while l <= r:
            m = l + (r - l)//2
            if A[m] > A[m-1] and A[m] > A[m+1]:
                return m
            elif A[m] > A[m-1] and A[m] < A[m+1]:
                l = m + 1
            else:
                r = m - 1
# @lc code=end