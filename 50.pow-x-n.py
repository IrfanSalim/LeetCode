#
# @lc app=leetcode id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n > 0:
            curr = self.myPow(x, n//2) 
            if n % 2 == 0:
                return curr * curr
            else:
                return curr * curr * x
        else:
            curr = 1 / self.myPow(x, -n//2) 
            if n % 2 == 0:
                return curr * curr
            else:
                return curr * curr * (1/x)
# @lc code=end

