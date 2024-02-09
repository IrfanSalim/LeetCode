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
    def isBalanced(self, root):
        def isBala(A):
            if not A:
                return [-1, True]
            
            l = isBala(A.left)
            r = isBala(A.right)

            if not l[1] or not r[1]:
                return [-1, False]
            elif abs(l[0] - r[0]) > 1:
                return [-1, False]
            else:
                return [max(l[0], r[0]) + 1, True]
            
        return isBala(root)[1]
    
    # isBal = True
    # def isBalanced(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     def height(A):
    #         if not A:
    #             return -1
    #         lh = height(A.left)
    #         rh = height(A.right)
    #         if abs(lh - rh) > 1:
    #             self.isBal = False
    #         return max(lh, rh) + 1
    #     height(root)
    #     return self.isBal      
# @lc code=end

