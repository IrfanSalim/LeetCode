#
# @lc app=leetcode id=73 lang=python
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        A = matrix
        n = len(A)
        m = len(A[0])
        for i in range(0,n):
            flag = 0
            for j in range(0,m):
                if A[i][j] == 0:
                    flag = 1
            if flag == 1:
                for j in range(0,m):
                    if A[i][j] != 0:
                        A[i][j] = "True"
        for j in range(0,m):
            flag = 0
            for i in range(0,n):
                if A[i][j] == 0:
                    flag = 1
            if flag == 1:
                for i in range(0,n):
                    if A[i][j] != 0:
                        A[i][j] = "True"
        for i in range(0,n):
            for j in range(0,m):
                if A[i][j] == "True": A[i][j] = 0
        return A
# @lc code=end

