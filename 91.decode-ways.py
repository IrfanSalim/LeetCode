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
        n = len(s)
        if s[0] == "0":
            return 0
        if n == 1:
            return 1
        lastChar = 1
        lastTwoChars = 1
        for i in range(1, n):
            one = int(s[i])
            two = int(s[i-1]) * 10 + one

            curr = 0
            if one > 0:
                curr += lastTwoChars
            if two >= 10 and two <= 26:
                curr += lastChar
            lastChar = lastTwoChars
            lastTwoChars = curr

        return lastTwoChars

        #------------------------------------------------------------------------------------------------------

        # bottom up DP with space
        # n = len(s)
        # dp = [0] * (n+1)
        # dp[n] = 1
        # for i in range(n-1, -1, -1):
        #     if s[i] == "0":
        #         continue
        #     else:
        #         dp[i] = dp[i+1]
        #         if i < n-1 and int(s[i] + s[i+1]) <= 26:
        #             dp[i] += dp[i+2]

        # return dp[0]

        #------------------------------------------------------------------------------------------------------

        # top down DP approach
        # dp = [0] * (len(s)+1)
        # def decode(i):
        #     if i < len(s) and s[i] == "0":
        #         return 0
        #     if i >= len(s)-1:
        #         return 1
        #     if dp[i] == 0:
        #         dp[i] = decode(i+1)
        #         if int(s[i]+s[i+1]) <= 26:
        #             dp[i] += decode(i+2)
        #     return dp[i]
        # return decode(0)
        
# @lc code=end

