#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#

# @lc code=start
from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = [[] for i in range(numCourses)]
        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])

        inDeg = [0] * numCourses
        for i in range(numCourses):
            for dep in adj[i]:
                inDeg[dep] += 1
        
        q = deque()
        for i in range(len(inDeg)):
            if not inDeg[i]:
                q.append(i)
        
        while q:
            ele = q.popleft()
            for n in adj[ele]:
                inDeg[n] -= 1
                if inDeg[n] == 0:
                    q.append(n)
        
        for i in range(len(inDeg)):
            if inDeg[i] != 0:
                return False
        
        return True
# @lc code=end

