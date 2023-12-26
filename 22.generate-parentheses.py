#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def par(st, n, open, close):
            if len(st) == 2 * n:
                ans.append(st)
            if open < n:
                par(st + "(", n, open+1, close)
            if close < open:
                par(st + ")", n, open, close+1)
        
        par("", n, 0, 0)

        return ans
        
# @lc code=end

