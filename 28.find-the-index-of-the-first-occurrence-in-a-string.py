#
# @lc app=leetcode id=28 lang=python
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if len(needle) == 1:
                    return i
                for j in range(i + 1, i + len(needle)):
                    if j < len(haystack):
                        if haystack[j] != needle[j - i]:
                            break
                        elif j - i + 1 == len(needle):
                            return i
        return -1
# @lc code=end

