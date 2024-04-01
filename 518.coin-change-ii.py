#
# @lc app=leetcode id=518 lang=python
#
# [518] Coin Change II
#

# @lc code=start
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0:
            return 1
        n = len(coins)
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in range(n):
            for j in range(1, amount+1):
                if coins[i] <= j:
                    dp[j] += dp[j - coins[i]]
        return dp[amount]
# @lc code=end

