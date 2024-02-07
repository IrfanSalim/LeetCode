#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        off = float('inf')
        ans = 0
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if abs(target - temp) < off:
                    ans = temp
                    off = abs(target - temp)
                if temp == target:
                    return target
                elif temp > target:
                    r -= 1
                else:
                    l += 1
        return ans

# @lc code=end

