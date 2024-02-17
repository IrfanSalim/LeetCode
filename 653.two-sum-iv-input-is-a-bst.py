#
# @lc app=leetcode id=653 lang=python
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        self.update(root, stack1, True)
        self.update(root, stack2, False)

        while stack1 and stack2:
            summ = stack1[-1].val + stack2[-1].val
            if stack1[-1].val == stack2[-1].val:
                return False
            elif summ == k:
                return True
            elif summ > k:
                ele = stack2.pop()
                self.update(ele.left, stack2, False)
            else:
                ele = stack1.pop()
                self.update(ele.right, stack1, True)

    def update(self, root, stack, flag):
        while root:
            stack.append(root)
            if flag:
                root = root.left
            else:
                root = root.right

# @lc code=end

