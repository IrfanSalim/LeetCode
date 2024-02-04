#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        i = n - 1
        while s[i] == " ":
            i -= 1
        while s[i] != " " and i >= 0:
            ans += 1
            i -= 1
        return ans
        
# @lc code=end

