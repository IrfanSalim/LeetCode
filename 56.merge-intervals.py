#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        n = len(intervals)
        curr = intervals[0]
        ans = []
        for i in range(1, n):
            if intervals[i][0] <= curr[1]:
                curr[1] = max(curr[1], intervals[i][1])
            else:
                ans.append(curr)
                curr = intervals[i]
        ans.append(curr)
        return ans
# @lc code=end

