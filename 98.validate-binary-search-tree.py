#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(root, s, e):
            if not root:
                return True
            left = valid(root.left, s, root.val - 1)
            right = valid(root.right, root.val + 1, e)
            if not left or not right:
                return False
            if root.val < s or root.val > e:
                return False
            return True
        return valid(root, float('-inf'), float('inf'))
        
# @lc code=end

