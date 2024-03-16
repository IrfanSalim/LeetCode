#
# @lc app=leetcode id=279 lang=python
#
# [279] Perfect Squares
#

# @lc code=start
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # returns True if the input number x is a square number,
        # else returns False
        def isSquare(x):
            sqRoot = int(math.sqrt(x));
            return (sqRoot * sqRoot == x);
        
        # Function to count minimum squares that sum to n
        def cntSquares(n):
        
            # ans = 1 if the number is a perfect square
            if (isSquare(n)):
                return 1;
            
            # ans = 2:
            # we check for each i if n - (i * i) is a perfect
            # square
            for i in range(1, int(math.sqrt(n))+1):
                if (isSquare(n - (i * i))):
                    return 2;
                
            # ans = 4
            # possible if the number is representable in the form
            # 4^a (8*b + 7).
            while (n % 4 == 0):
                n >>= 2;
            
            if (n % 8 == 7):
                return 4;
            
            # since all the other cases have been evaluated, the
            # answer can only then be 3 if the program reaches here
            return 3;

        return cntSquares(n)
        # recursive top-down approach
        # dp = [-1] * (n+1)
        # def minSquares(A):
        #     if A <= 3:
        #         return A
        #     if dp[A] != -1:
        #         return dp[A]
        #     x = 1
        #     ans = A
        #     while x*x <= A:
        #         ans = min(ans, minSquares(A - (x*x)))
        #         x += 1
        #     dp[A] = ans + 1
        #     return dp[A]
        # return minSquares(n)
        
# @lc code=end

