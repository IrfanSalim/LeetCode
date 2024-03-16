#
# @lc app=leetcode id=2078 lang=python
#
# [2078] Two Furthest Houses With Different Colors
#

# @lc code=start
class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        ans = -1
        for i in range(len(colors)):
            if colors[i] != colors[0]: ans = max(ans, i)
            if colors[i] != colors[-1]: ans = max(ans, len(colors) - i - 1)
        return ans
# @lc code=end