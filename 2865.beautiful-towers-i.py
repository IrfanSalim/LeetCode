#
# @lc app=leetcode id=2865 lang=python
#
# [2865] Beautiful Towers I
#

# @lc code=start
class Solution(object):
    def maximumSumOfHeights(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        maxSum = 0
        for i in range(n):
            curSum = heights[i]
            maxLeft = heights[i]
            for j in range(i-1, -1, -1):
                maxLeft = min(maxLeft, heights[j])
                curSum += maxLeft

            maxRight = heights[i]
            for k in range(i+1, n):
                maxRight = min(maxRight, heights[k])
                curSum += maxRight

            maxSum = max(maxSum, curSum)
        
        return maxSum

# @lc code=end

