#
# @lc app=leetcode id=543 lang=python
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dia = [0]
        def height(A):
            if not A:
                return -1
            left = height(A.left)
            right = height(A.right)
            dia[0] = max(dia[0], left + right + 2)
            return max(left, right) + 1
        height(root)
        return dia[0]
        
# @lc code=end

