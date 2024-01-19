#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#

# @lc code=start
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = [float('inf')]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if val <= self.min[-1]:
            self.min.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.stack and self.stack[-1] == self.min[-1]:
            self.min.pop()
        if self.stack: self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if self.stack else 0

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1] if len(self.min) > 1 else 0


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

