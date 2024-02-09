#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    isBal = True
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def height(A):
            if not A:
                return -1
            lh = height(A.left)
            rh = height(A.right)

            if abs(lh - rh) > 1:
                self.isBal = False
            
            return max(lh, rh) + 1

        height(root)
        return self.isBal      
# @lc code=end

