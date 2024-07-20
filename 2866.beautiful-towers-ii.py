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


        # # for each possible peek, compute maximum sum of heights;
        # # this is achieved by maintaining a monotonic stack with 
        # # heights and counts 
        
        # def find_peak(arr):

        #     stack, acc = [], 0
        #     peeks = []

        #     for height in arr:
        #         count = 1
        #         while stack and height <= stack[-1][0]:
        #             h, c = stack.pop()
        #             acc -= h * c
        #             count += c
        #         stack.append((height, count))
        #         acc += height * count
        #         peeks.append(acc)
        #     return peeks

        # # precompute sums both from both tails (forward and reverse)
        # fwd = [0] + find_peak(maxHeights)
        # rev = find_peak(maxHeights[::-1])[::-1] + [0]

        # # the answer is the maximum sum for two tails
        # return max(f + r for f, r in zip(fwd, rev))
# @lc code=end

