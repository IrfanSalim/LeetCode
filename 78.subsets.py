#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        arr = []
        def backtrack(i):
            ans.append(arr[:])

            for j in range(i, len(nums)):
                arr.append(nums[j])
                backtrack(j + 1)
                arr.pop()

        backtrack(0)
        return ans
# @lc code=end

