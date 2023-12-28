#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        i, j = 0, len(height)-1
        while i < j:
            ht = min(height[i], height[j])
            wd = j - i
            ans = max(ans, ht * wd)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans
        
# @lc code=end

