#
# @lc app=leetcode id=958 lang=python
#
# [958] Check Completeness of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = deque()
        q.append(root)
        gap = False
        while q:
            ele = q.popleft()
            if not ele:
                gap = True
            else:
                if gap: return False
                q.append(ele.left)
                q.append(ele.right)
        return True
# @lc code=end

