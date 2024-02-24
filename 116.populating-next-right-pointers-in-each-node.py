#
# @lc app=leetcode id=116 lang=python
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        curr = root
        while curr.left:
            temp = curr
            while temp:
                temp.left.next = temp.right
                if temp.next:
                    temp.right.next = temp.next.left
                temp = temp.next
            curr = curr.left
        return root

        # basic approach to use level order traversal with help of deque
        # q = deque()
        # q.append(root)
        # while q:
        #     sz = len(q)
        #     for i in range(sz):
        #         ele = q.popleft()
        #         if i != sz - 1:
        #             ele.next = q[0]
        #         if ele.left:
        #             q.append(ele.left)
        #         if ele.right:
        #             q.append(ele.right)
        # return root
# @lc code=end

