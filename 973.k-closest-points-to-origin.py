#
# @lc app=leetcode id=973 lang=python
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # sorting solution
        if k == len(points):
            return points
        points = sorted(points, key = lambda points: points[0] ** 2 + points[1] ** 2)
        return points[:k]
    
        # max heap solution
        # heap = []
        # for i in range(k):
        #     dist = points[i][0]**2 + points[i][1]**2
        #     heapq.heappush(heap, (-dist, points[i][0], points[i][1]))
        
        # for j in range(k, len(points)):
        #     dist = points[j][0]**2 + points[j][1]**2
        #     if dist < -heap[0][0]:
        #         heapq.heappush(heap, (-dist, points[j][0], points[j][1]))
        #         heapq.heappop(heap)
        
        # heap = [[point[1], point[2]] for point in heap]
        # return heap
# @lc code=end

