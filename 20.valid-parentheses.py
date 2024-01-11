#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brac = {")":"(", "}":"{", "]":"["}
        bracklist = list(brac.values())
        stack = []
        for i in range(len(s)):
            if s[i] in bracklist:
                stack.append(s[i])
            else:
                if not len(stack) or brac[s[i]] != stack.pop():
                    return 0
        return 0 if len(stack) else 1
        
# @lc code=end

