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
        left, right = 0, n
        top, bottom = 0, m

        ans = []

        while left < right and top < bottom:
            # left to right
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1

            # top to bottom
            for j in range(top, bottom):
                ans.append(matrix[j][right-1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # right to left
            for i in range(right-1, left-1, -1):
                ans.append(matrix[bottom-1][i])
            bottom -= 1

            # bottom to top
            for j in range(bottom-1, top-1, -1):
                ans.append(matrix[j][left])
            left += 1
        
        return ans
# @lc code=end

