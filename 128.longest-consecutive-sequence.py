#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # approach using hashset
        numSet = set(nums)
        ans = 0
        for num in nums:
            if not num-1 in numSet:
                temp = num
                len = 1
                while temp+1 in numSet:
                    temp += 1
                    len += 1
                ans = max(ans, len)
        return ans

        # approach using hashmap
        # rangeMap = {}
        # ans = 0
        # for num in nums:
        #     start, end = num, num
        #     if num + 1 in rangeMap:
        #         start = rangeMap[num+1][0]
                
        #     if num - 1 in rangeMap:
        #         end = rangeMap[num-1][1]
                
        #     if num + 1 in rangeMap:
        #         rangeMap[num+1][1] = min(rangeMap[num+1][1], end)
        #         rangeMap[num+1][0] = max(rangeMap[num+1][0], start)
        #     if num - 1 in rangeMap:
        #         rangeMap[num-1][1] = min(rangeMap[num-1][1], end)
        #         rangeMap[num-1][0] = max(rangeMap[num-1][0], start)
            
        #     if start in rangeMap:
        #         rangeMap[start][1] = min(rangeMap[start][1], end)
        #         rangeMap[start][0] = max(rangeMap[start][0], start)        
            
        #     if end in rangeMap:
        #         rangeMap[end][1] = min(rangeMap[end][1], end)
        #         rangeMap[end][0] = max(rangeMap[end][0], start)
            
        #     rangeMap[num] = [start, end]
        #     ans = max(ans, start - end + 1)
        # return ans
# @lc code=end

