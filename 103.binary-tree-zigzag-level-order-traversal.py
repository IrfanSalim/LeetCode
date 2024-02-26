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
        flag = True
        while q:
            sz = len(q)
            temp = [0] * sz
            for i in range(sz):
                ele = q.popleft()
                idx = i if flag else sz - i - 1
                temp[idx] = ele.val
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
            ans.append(temp)
            flag = not flag
        return ans
# @lc code=end

