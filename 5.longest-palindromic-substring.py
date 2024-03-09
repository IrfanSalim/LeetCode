#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = 0
        si, ei = 0, 0
        for i in range(len(s)):
            p1 = i
            p2 = i
            length = self.expand(p1, p2, s)
            if length[0] > ans:
                ans = length[0]
                si = length[1]
                ei = length[2]

        for i in range(len(s) - 1):
            p1 = i
            p2 = i+1
            length = self.expand(p1, p2, s)
            if length[0] > ans:
                ans = length[0]
                si = length[1]
                ei = length[2]

        return s[si+1:ei]

    def expand(self, p1, p2, s):
        while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
            p1 -= 1
            p2 += 1
        return [p2 - p1 + 1, p1, p2]
# @lc code=end

