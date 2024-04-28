#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        
        return ans

        # value = 0
        # prev = 0
        # for ch in s:
        #     if ch == 'I':
        #         value += 1
        #         prev = 1
        #     elif ch == 'V':
        #         value += 3 if prev == 1 else 5
        #         prev = 5
        #     elif ch == 'X':
        #         value += 8 if prev == 1 else 10
        #         prev = 10
        #     elif ch == 'L':
        #         value += 30 if prev == 10 else 50
        #         prev = 50
        #     elif ch == 'C':
        #         value += 80 if prev == 10 else 100
        #         prev = 100
        #     elif ch == 'D':
        #         value += 300 if prev == 100 else 500
        #         prev = 500
        #     elif ch == 'M':
        #         value += 800 if prev == 100 else 1000
        #         prev = 1000
        # return value
# @lc code=end

