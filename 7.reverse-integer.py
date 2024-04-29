#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # remainder approach
        is_negative = False

        if x < 0:
            is_negative = True
            x *= -1
        
        res = 0
        while x > 0:
            res = (res * 10) + (x % 10)
            x //= 10
        
        if res > 2 ** 31 - 1:
            return 0
        
        return res * -1 if is_negative else res

        # approach with converting num to string and reversion
        # res = 0
        # if x < 0:
        #     res = int(str(x)[1:][::-1]) * -1
        # else:
        #     res = int(str(x)[::-1])
        
        # if res > 2 ** 31 - 1 or res < -2 ** 31:
        #     return 0
        
        # return res
# @lc code=end

