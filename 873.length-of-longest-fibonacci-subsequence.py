#
# @lc app=leetcode id=873 lang=python
#
# [873] Length of Longest Fibonacci Subsequence
#

# @lc code=start
class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # optimized dp solution
        A = arr
        n = len(A)
        dp = [[2] * (n) for _ in range(n)]
        indexes = {x: i for i,x in enumerate(A)}
        for j in range(n):
            for i in range(j):
                req = A[j] - A[i]
                if req in indexes and indexes[req] < i:
                    k = indexes[req]
                    dp[i][j] = max(dp[i][j], 1 + dp[k][i])
        ans = max([max(n) for n in dp])
        return ans if ans > 2 else 0

        # brute force solution with n^3 TC
        # A = arr
        # n = len(A)
        # dp = [[2 for _ in range(n+1)] for _ in range(n+1)]
        # for j in range(n):
        #     for i in range(j):
        #         for k in range(i):
        #             if A[k]+A[i] == A[j]:
        #                 dp[i][j] = max(dp[i][j], 1+dp[k][i])
        # ans = max([max(n) for n in dp])
        # return 0 if ans <= 2 else ans
# @lc code=end

