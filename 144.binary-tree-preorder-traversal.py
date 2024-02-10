#
# @lc app=leetcode id=144 lang=python
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        def preorder(A):
            if not A:
                return
            ans.append(A.val)
            preorder(A.left)
            preorder(A.right)
        preorder(root)
        return ans
# @lc code=end

