#
# @lc app=leetcode id=115 lang=python
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(s)
        m = len(t)

        if n < m: return 0

        dp = [1] + [0] * m

        for i in range(n):
            for j in reversed(range(m)):
                if s[i] == t[j]:
                    dp[j + 1] += dp[j]

        return dp[m] 
# @lc code=end
        

# # Top Down approach

# class Solution:
#     # @param A : string
#     # @param B : string
#     # @return an integer
#     def helper(self, dp, i, j, A, B):
#         if dp[i][j] != -1: return dp[i][j]

#         # B is empty
#         if j == 0:
#             dp[i][j] = 1

#         # A is empty
#         elif i == 0:
#             dp[i][j] = 0

#         else:
#             # current characters don’t match
#             if A[i - 1] != B[j - 1]:
#                 dp[i][j] = self.helper(dp, i - 1, j, A, B)

#             # current characters match
#             else:
#                 dp[i][j] = self.helper(dp, i - 1, j, A, B) + self.helper(dp, i - 1, j - 1, A, B)

#         return dp[i][j]

#     def numDistinct(self, A, B):
#         n = len(A)
#         m = len(B)

#         if n < m: return 0

#         dp = [[-1] * (m + 1) for _ in range(n + 1)]
#         return self.helper(dp, n, m, A, B)

#     # TC: O(MN); SC: O(MN)


# # Top Down approach

# class Solution:
#     # @param A : string
#     # @param B : string
#     # @return an integer
#     def helper(self, dp, i, j, A, B, n, m):
#         if dp[i][j] != -1: return dp[i][j]

#         # B is full
#         if j == m:
#             dp[i][j] = 1

#         # A is full
#         elif i == n:
#             dp[i][j] = 0

#         else:
#             # current characters don’t match
#             if A[i] != B[j]:
#                 dp[i][j] = self.helper(dp, i + 1, j, A, B, n, m)

#             # current characters match
#             else:
#                 dp[i][j] = self.helper(dp, i + 1, j, A, B, n, m) + self.helper(dp, i + 1, j + 1, A, B, n, m)

#         return dp[i][j]

#     def numDistinct(self, A, B):
#         n = len(A)
#         m = len(B)

#         if n < m: return 0

#         dp = [[-1] * (m + 1) for _ in range(n + 1)]
#         return self.helper(dp, 0, 0, A, B, n, m)

#     # TC: O(MN); SC: O(MN)


# # Bottom Up approach

# class Solution:
#     # @param A : string
#     # @param B : string
#     # @return an integer
#     def numDistinct(self, A, B):
#         n = len(A)
#         m = len(B)

#         if n < m: return 0

#         dp = [[0] * (m + 1) for _ in range(n + 1)]

#         for i in range(n + 1):
#             for j in range(m + 1):
#                 if j == 0:
#                     dp[i][j] = 1
#                     continue

#                 if A[i - 1] != B[j - 1]:
#                     dp[i][j] = dp[i - 1][j]
#                 else:
#                     dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

#         return dp[n][m]

#         # TC: O(MN); SC: O(MN)


# # Bottom Up approach - optimised

# class Solution:
#     # @param A : string
#     # @param B : string
#     # @return an integer
#     def numDistinct(self, A, B):
#         n = len(A)
#         m = len(B)

#         if n < m: return 0

#         proc = [0] * (m + 1)
#         stor = proc.copy()
#         proc[0], stor[0] = 1, 1

#         for i in range(n):
#             proc = [0] * (m + 1)
#             proc[0] = 1
#             for j in range(1, m + 1):
#                 if A[i] != B[j - 1]:
#                     proc[j] = stor[j]
#                 else:
#                     proc[j] = stor[j] + stor[j - 1]

#             stor = proc

#         return stor[m]

#         # TC: O(MN); SC: O(M)


# # Bottom Up approach - super optimised

# class Solution:
#     # @param A : string
#     # @param B : string
#     # @return an integer
#     def numDistinct(self, A, B):
#         n = len(A)
#         m = len(B)

#         if n < m: return 0

#         dp = [1] + [0] * m

#         for i in range(n):
#             for j in reversed(range(m)):
#                 if A[i] == B[j]:
#                     dp[j + 1] += dp[j]

#         return dp[m] 

#         # TC: O(MN); SC: O(M)

