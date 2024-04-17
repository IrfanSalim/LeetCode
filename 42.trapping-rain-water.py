#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        lmax, rmax = height[left], height[right]
        ans = 0
        while left < right:
            lmax = max(lmax, height[left])
            rmax = max(rmax, height[right])
            if lmax < rmax:
                ans += min(lmax, rmax) - height[left]
                left += 1
            else:
                ans += min(lmax, rmax) - height[right]
                right -= 1
        return ans
# @lc code=end

