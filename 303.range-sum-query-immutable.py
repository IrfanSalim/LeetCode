#
# @lc app=leetcode id=303 lang=python
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.num = nums
        self.pf = [self.num[0]]
        for i in range(1, len(self.num)):
            self.pf.append(self.pf[i-1] + self.num[i])

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        summ = self.pf[right]
        if left > 0:
            summ -= self.pf[left-1]
        return summ
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

