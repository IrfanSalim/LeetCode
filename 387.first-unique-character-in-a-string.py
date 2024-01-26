#
# @lc app=leetcode id=387 lang=python
#
# [387] First Unique Character in a String
#

# @lc code=start
from collections import deque

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = [0] * 26
        for char in s:
            freq[ord(char) - 97] += 1
        
        for i in range(len(s)):
            if freq[ord(s[i]) - 97] == 1:
                return i
        
        return -1
        
# @lc code=end

