#
# @lc app=leetcode id=322 lang=python
#
# [322] Coin Change
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        n = len(coins)
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(n):
                if coins[j] <= i:
                    dp[i] = min(dp[i], 1+dp[i - coins[j]])
        return dp[amount] if dp[amount] != float('inf') else -1


        # top down DP approach
        # n = len(coins)
        # dp = [-1] * (amount+1)

        # def minCoins(j):
        #     if j < 0:
        #         return float('inf')
        #     if j == 0:
        #         return 0
        #     if dp[j] == -1:
        #         dp[j] = float('inf')
        #         for i in range(n):
        #             dp[j] = min(dp[j], 1 + minCoins(j-coins[i]))
        #     return dp[j]
        # ans = minCoins(amount) 
        # return ans if ans != float('inf') else -1
# @lc code=end

