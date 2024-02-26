#
# @lc app=leetcode id=103 lang=python
#
# [103] Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []
        while q:
            sz = len(q)
            temp = []
            for i in range(sz):
                ele = q.popleft()
                temp.append(ele.val)
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
            if len(ans) % 2:
                temp = temp[::-1]
            ans.append(temp)
        return ans
# @lc code=end

