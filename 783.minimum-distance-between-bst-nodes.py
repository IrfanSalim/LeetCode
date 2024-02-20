#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        minSoFar = float('inf')
        prev = float('-inf')

        def recur(node):
            nonlocal minSoFar
            nonlocal prev
            
            if not node:
                return 
            
            recur(node.left)
            minSoFar = min(minSoFar, node.val - prev)
            prev = node.val
            recur(node.right)

        recur(root)
        return minSoFar

# @lc code=end

