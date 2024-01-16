#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        A = nums
        n = len(A)
        l, h = 0, n-1
        ans = [-1, -1]
        
        #find the first index using BS
        while l <= h:
            m = l + (h - l)//2
            if A[m] == target:
                ans[0] = m
                h = m - 1
            elif A[m] > target:
                h = m - 1
            else:
                l = m + 1
        
        #find the last index using BS
        l, h = 0, n-1
        while l <= h:
            m = l + (h - l)//2
            if A[m] == target:
                ans[1] = m
                l = m + 1
            elif A[m] > target:
                h = m - 1
            else:
                l = m + 1
        
        return ans
# @lc code=end

