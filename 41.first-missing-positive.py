#
# @lc app=leetcode id=41 lang=python
#
# [41] First Missing Positive
#

# @lc code=start
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = nums
        i = 0
        n = len(A)
        while i < n:
            if A[i] >= 1 and A[i] <= n+1:
                correct_idx = A[i]-1
                if correct_idx < n and A[correct_idx] != A[i]:
                    A[correct_idx], A[i] = A[i], A[correct_idx]
                else:
                    i += 1
            else:
                i += 1
        
        for i in range(n):
            if A[i] != i+1: return i+1
        return n+1

        # approach using set
        # nums = set(nums)
        # x = 1
        # while x in nums:
        #     x += 1
        # return x
# @lc code=end

