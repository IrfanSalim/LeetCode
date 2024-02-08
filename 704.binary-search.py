#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
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
        l, h = 0, n - 1
        while l <= h:
            mid = l + (h - l)//2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        return -1
        
# @lc code=end

