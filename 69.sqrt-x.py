#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, h = 1, x
        ans = 0
        while l <= h:
            m = l + (h-l)//2
            if m*m == x:
                return m
            elif m*m < x:
                ans = m
                l = m+1
            else:
                h = m-1
        return ans
# @lc code=end

