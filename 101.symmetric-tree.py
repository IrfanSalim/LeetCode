#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        def check(A, B):
            if not A and not B:
                return True
            elif not A or not B:
                return False
            elif A.val != B.val:
                return False
            return check(A.left, B.right) and check(A.right, B.left)
        return check(root, root)    
        
# @lc code=end

