#
# @lc app=leetcode id=941 lang=python
#
# [941] Valid Mountain Array
#

# @lc code=start
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) <= 2:
            return False
        i = 0
        while i < len(arr) - 1 and arr[i + 1] > arr[i]:
            i += 1
        if i == 0 or i == len(arr) - 1:
            return False
        while i < len(arr) - 1 and arr[i + 1] < arr[i]:
            i += 1
        if i == len(arr) - 1:
            return True
        return False
# @lc code=end

