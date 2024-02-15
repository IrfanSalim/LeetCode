#
# @lc app=leetcode id=344 lang=python
#
# [344] Reverse String
#

# @lc code=start
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l, h = 0, len(s) - 1
        while l < h:
            s[l], s[h] = s[h], s[l]
            l += 1
            h -= 1
        return s
# @lc code=end

