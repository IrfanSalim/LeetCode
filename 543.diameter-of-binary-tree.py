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
        # approach with a pair return
        def diameter(A):
            if not A:
                return [-1, 0]
            left = diameter(A.left)
            right = diameter(A.right)
            ht = max(left[0], right[0]) + 1
            dia = max(left[1], right[1], left[0] + right[0] + 2)
            return [ht, dia]
        
        return diameter(root)[1]

        # approach with a global variable
        # dia = [0]
        # def height(A):
        #     if not A:
        #         return -1
        #     left = height(A.left)
        #     right = height(A.right)
        #     dia[0] = max(dia[0], left + right + 2)
        #     return max(left, right) + 1
        # height(root)
        # return dia[0]
        
# @lc code=end

