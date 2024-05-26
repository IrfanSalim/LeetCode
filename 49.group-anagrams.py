#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = {}
        strs.sort()
        for str in strs:
            key = [0] * 26
            for c in str:
                key[ord(c) - ord('a')] += 1
            key = tuple(key)
            if not key in group:
                group[key] = []
            group[key].append(str)

        return group.values()
# @lc code=end

