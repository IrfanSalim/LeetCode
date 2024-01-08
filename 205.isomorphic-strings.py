#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        chars = {}
        chart = {}

        for i in range(len(s)):
            if s[i] in chars:
                if chars[s[i]] != t[i]: 
                    return False
            else:
                chars[s[i]] = t[i]

            if t[i] in chart:
                if chart[t[i]] != s[i]: 
                    return False
            else:
                chart[t[i]] = s[i]

        return True

# @lc code=end

