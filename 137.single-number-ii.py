#
# @lc app=leetcode id=137 lang=python
#
# [137] Single Number II
#

# @lc code=start
from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # bit manipulation approach
        # ones is a bitmask to represent the ith bit had appeared once
        ones = 0
        # twos is a bitmask to represent the ith bit had appeared twice
        twos = 0
        common_mask = 0
        for a in nums:
            twos |= ones & a
            ones ^= a
            common_mask = ~(ones & twos)
            ones &= common_mask
            twos &= common_mask
        return ones

        # ans = 0
        # for i in range(32):
        #     count = 0
        #     for num in nums:
        #         if (num & (1 << i)) > 0:
        #             count += 1
        #     if count % 3 == 1:
        #         ans |= (1 << i)
        # return ans

        # brute force approach
        # count = Counter(nums)
        # for key in count:
        #     if count[key] == 1:
        #         return key
# @lc code=end

