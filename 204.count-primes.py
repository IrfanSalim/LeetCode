#
# @lc app=leetcode id=204 lang=python
#
# [204] Count Primes
#

# @lc code=start
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        
        primes = [True] * n
        primes[0] = primes[1] = False
        cnt = 1

        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n, i):
                    if primes[j]:
                        cnt += 1
                    primes[j] = False

        return n - cnt - 1
        # arr = [True] * (n + 1)
        # for i in range(2, int(n**0.5) + 1):
        #     if arr[i]:
        #         j = i * i
        #         while j <= n:
        #             arr[j] = False
        #             j += i
        #     i += 1
        # count = 0
        # for i in range(2, n):
        #     if arr[i]:
        #         count += 1
        # return count
# @lc code=end

