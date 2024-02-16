#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]
        profit = 0
        for i in range(len(prices)):
            if minPrice > prices[i]:
                minPrice = prices[i]
            currProfit = prices[i] - minPrice
            profit = max(profit, currProfit)
        return profit
# @lc code=end

