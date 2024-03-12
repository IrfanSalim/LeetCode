#
# @lc app=leetcode id=378 lang=python
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Binary search approach
        m, n = len(matrix), len(matrix[0])

        def countLessOrEqual(num):
            count = 0
            for i in range(m):
                if matrix[i][0] > num:
                    break
                for j in range(n):
                    if matrix[i][j] <= num:
                        count += 1
                    else:
                        break
            return count
        
        left, right = matrix[0][0], matrix[m-1][n-1]
        ans = -1
        while left <= right:
            mid = left + (right - left)//2

            if countLessOrEqual(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

        #--------------------------------------------------------------------------------------------------------

        # using Min heap
        # heap = []
        # m, n = len(matrix), len(matrix[0])
        # for row in range(min(k, m)):
        #     heapq.heappush(heap, (matrix[row][0], row, 0))
        
        # for i in range(k):
        #     val, row, column = heapq.heappop(heap)
        #     if column + 1 < n:
        #         heapq.heappush(heap, (matrix[row][column+1], row, column+1))

        # return val

        # -------------------------------------------------------------------------------------------------------
        
        # using Max heap
        # heap = []
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if len(heap) < k:
        #             heapq.heappush(heap, -matrix[i][j])
        #         else:
        #             if matrix[i][j] < -heap[0]:
        #                 heapq.heappop(heap)
        #                 heapq.heappush(heap, -matrix[i][j])
        # return -heap[0]
# @lc code=end

