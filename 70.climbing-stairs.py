#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev, curr = 0, 1
        for i in range(n):
            next = prev + curr
            prev = curr
            curr = next
        return curr
        
# @lc code=end

