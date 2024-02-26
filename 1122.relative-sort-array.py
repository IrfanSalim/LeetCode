#
# @lc app=leetcode id=1122 lang=python
#
# [1122] Relative Sort Array
#

# @lc code=start
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        arr1.sort()
        ans = []
        freq = {}
        for ele in arr1:
            freq[ele] = freq.get(ele, 0) + 1
        for ele in arr2:
            if ele in freq:
                ans += [ele] * freq[ele]
                freq[ele] = 0
        for ele in arr1:
            if freq[ele] > 0 and ele not in arr2:
                ans += [ele] * freq[ele]
                freq[ele] = 0
        return ans
# @lc code=end

