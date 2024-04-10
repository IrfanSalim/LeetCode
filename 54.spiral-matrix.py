#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, 0
        ans = []
        while m > 1 and n > 1:
            hor = m-1
            ver = n-1
            while j < ver:
                ans.append(matrix[i][j])
                j += 1
            while i < hor:
                ans.append(matrix[i][j])
                i += 1
            while j > 0:
                ans.append(matrix[i][j])
                j -= 1
            while i > 0:
                ans.append(matrix[i][j])
                i -= 1
            i += 1
            j += 1
            n -= 2
            m -= 2
        if n == 1 or m == 1:
            ans.append(matrix[i][j])
        return ans
# @lc code=end

