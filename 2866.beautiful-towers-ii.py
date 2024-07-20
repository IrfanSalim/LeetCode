#
# @lc app=leetcode id=2866 lang=python
#
# [2866] Beautiful Towers II
#

# @lc code=start
class Solution(object):
    def maximumSumOfHeights(self, maxHeights):
        """
        :type maxHeights: List[int]
        :rtype: int
        """
        n = len(maxHeights)
        smallRight = [n] * n
        smallLeft = [-1] * n
        stack = [0]
        for i in range(1, n):
            while stack and maxHeights[stack[-1]] >= maxHeights[i]:
                stack.pop()
            if stack:
                smallLeft[i] = stack[-1]
            stack.append(i)
        
        stack = [n-1]
        for i in range(n-2, -1, -1):
            while stack and maxHeights[stack[-1]] >= maxHeights[i]:
                stack.pop()
            if stack:
                smallRight[i] = stack[-1]
            stack.append(i)
        
        prefix = [0] * n
        for i in range(n):
            prefix[i] = (i - smallLeft[i]) * maxHeights[i]
            if smallLeft[i] != -1:
                prefix[i] += prefix[smallLeft[i]]
        
        suffix = [0] * n
        for i in range(n-1, -1, -1):
            suffix[i] = (smallRight[i] - i) * maxHeights[i]
            if smallRight[i] != n:
                suffix[i] += suffix[smallRight[i]]
        
        maxSum = max(prefix[n-1], suffix[0])
        for i in range(n-1):
            maxSum = max(maxSum, prefix[i] + suffix[i+1])

        return maxSum

# @lc code=end

