#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n, m = len(matrix), len(matrix[0])
        i, j = 0, n * m - 1
        while i <= j:
            mid = i + (j - i)//2
            tmpi = mid // m
            tmpj = mid % m
            ele = matrix[tmpi][tmpj]
            if ele == target:
                return True
            elif ele > target:
                j = mid - 1
            else:
                i = mid + 1
        return False

# @lc code=end

