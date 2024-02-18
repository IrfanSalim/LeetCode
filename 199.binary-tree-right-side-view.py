#
# @lc app=leetcode id=199 lang=python
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        maxLevel = [0]
        ans = []
        def right(A, level):
            if not A:
                return
            if level > maxLevel[0]:
                ans.append(A.val)
                maxLevel[0] = level
            right(A.right, level + 1)
            right(A.left, level + 1)
        right(root, 1)
        return ans
# @lc code=end

