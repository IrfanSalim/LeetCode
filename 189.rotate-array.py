#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        def reverse(A, s, e):
            i, j = s, e
            while i <= j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        k = k % n
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)
        return nums

# @lc code=end

