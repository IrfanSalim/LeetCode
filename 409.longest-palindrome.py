#
# @lc app=leetcode id=409 lang=python
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        ans = 0
        odd = False
        for n in s:
            freq[n] = freq.get(n, 0) + 1
        for key in freq.keys():
            if freq[key] % 2 == 0:
                ans += freq[key]
            else:
                ans += freq[key]-1
                odd = True
        if odd:
            return ans+1
        return ans
# @lc code=end

