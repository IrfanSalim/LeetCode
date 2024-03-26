#
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s)+1)
        def decode(i):
            if i < len(s) and s[i] == "0":
                return 0
            if i >= len(s)-1:
                return 1
            if dp[i] == 0:
                dp[i] = decode(i+1)
                if int(s[i]+s[i+1]) <= 26:
                    dp[i] += decode(i+2)
            return dp[i]
        return decode(0)
        
# @lc code=end

