#
# @lc app=leetcode id=105 lang=python
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, A, B):
        if not A or not B:
            return None
       
        root_val = A[0]
        root = TreeNode(root_val)
       
        # find the index of the root in the inorder traversal
        root_idx = B.index(root_val)
       
        # recursively construct the left and right subtrees
        root.left = self.buildTree(A[1:root_idx+1], B[:root_idx])
        root.right = self.buildTree(A[root_idx+1:], B[root_idx+1:])
       
        return root
# @lc code=end

