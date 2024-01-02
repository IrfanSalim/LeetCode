#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate elements
                continue
            l, r = i + 1, n - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if temp == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    # Skip duplicate elements
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif temp > 0:
                    r -= 1
                else:
                    l += 1
        return ans

# @lc code=end

