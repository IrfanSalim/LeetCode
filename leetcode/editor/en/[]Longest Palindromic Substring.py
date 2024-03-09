# Given a string s, return the longest palindromic substring in s. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "cbbd"
# Output: "bb"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s consist of only digits and English letters. 
#  
# 
#  Related Topics String Dynamic Programming 👍 28714 👎 1717


# leetcode submit region begin(Prohibit modification and deletion)
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
        
# leetcode submit region end(Prohibit modification and deletion)
