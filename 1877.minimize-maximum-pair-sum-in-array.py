#
# @lc app=leetcode id=1877 lang=python
#
# [1877] Minimize Maximum Pair Sum in Array
#

# @lc code=start
class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        min_max_sum = 0
        for i in range(len(nums) // 2):
            min_max_sum = max(min_max_sum, nums[i] + nums[len(nums) - 1 - i])
            
        return min_max_sum
        
# @lc code=end

