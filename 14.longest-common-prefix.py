#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ''

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]

        # prev = strs[0]
        # pf = len(strs[0])
        # for i in range(1, len(strs)):
        #     n = len(strs[i])
        #     if n == 0:
        #         return ""
        #     if n < pf:
        #         pf = n
        #     while pf and prev[:pf] != strs[i][:pf]:
        #         pf -= 1
        #     if pf == 0:
        #         return ""
        #     prev = strs[i]
        # return prev[:pf]
# @lc code=end

