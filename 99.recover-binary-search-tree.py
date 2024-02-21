#
# @lc app=leetcode id=99 lang=python
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        prev = None
        first = None
        second = None
        curr = root
        while curr:
            if not curr.left:
                if prev:
                    if prev.val > curr.val:
                        if not first:
                            first = prev
                            second = curr
                        else:
                            second = curr
                prev = curr
                curr = curr.right
            else:
                temp = curr.left
                while temp.right and temp.right != curr:
                    temp = temp.right
                if not temp.right:
                    temp.right = curr
                    curr = curr.left
                else:
                    temp.right = None
                    if prev:
                        if prev.val > curr.val:
                            if not first:
                                first = prev
                                second = curr
                            else:
                                second = curr
                    prev = curr
                    curr = curr.right
        first.val, second.val = second.val, first.val


        # basic approach with O(N) space
        # def inorder(A):
        #     if not A:
        #         return
        #     inorder(A.left)
        #     if self.prev:
        #         if A.val < self.prev.val:
        #             if not self.first:
        #                 self.first = self.prev
        #                 self.second = A
        #             else:
        #                 self.second = A
        #     self.prev = A
        #     inorder(A.right)
        # inorder(root)
        # self.second.val, self.first.val = self.first.val, self.second.val
        
# @lc code=end

