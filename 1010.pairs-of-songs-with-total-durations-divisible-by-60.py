#
# @lc app=leetcode id=1010 lang=python
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#

# @lc code=start
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        freq = {}
        pairs = 0
        for t in time:
            remainder = t % 60
            complement = (60 - remainder) % 60
            if complement in freq:
                pairs += freq[complement]
            freq[remainder] = freq.get(remainder, 0) + 1
        return pairs
# @lc code=end

