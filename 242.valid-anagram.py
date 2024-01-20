#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        freqS = {}
        freqT = {}
        for i in s:
            freqS[i] = freqS.get(i, 0) + 1
        for j in t:
            freqT[j] = freqT.get(j, 0) + 1
        
        for key in freqS:
            if key in freqT:
                if freqS[key] != freqT[key]:
                    return False
            else:
                return False
        return True

# @lc code=end

