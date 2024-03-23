#
# @lc app=leetcode id=1235 lang=python
#
# [1235] Maximum Profit in Job Scheduling
#

# @lc code=start
class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        A = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        A.sort()
        dp = [-1] * (len(A) + 1)
        def dfs(i):
            if i == len(A):
                return 0
            if dp[i] != -1:
                return dp[i]
            no = dfs(i+1)
            j = self.find(A, i)
            yes = A[i][2]
            if j != -1:
                yes += dfs(j)
            dp[i] = max(yes, no)
            return dp[i]
        
        return dfs(0)
    
    def find(self, A, i):
        l, h = i + 1, len(A) - 1
        ans = -1
        while l <= h:
            m = l + (h - l) // 2
            if A[m][0] >= A[i][1]:
                ans = m
                h = m - 1
            else:
                l = m + 1
        return ans

# @lc code=end

