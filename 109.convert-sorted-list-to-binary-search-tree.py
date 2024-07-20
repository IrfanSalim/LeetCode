#
# @lc app=leetcode id=109 lang=python
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        n = 0
        self.head = head
        curr = head
        while curr:
            curr = curr.next
            n += 1
        return self.rec(0, n-1)
    
    def rec(self, st, end):
        if st > end:
            return None
        
        #find the mid point of the list
        mid = (st + end) // 2

        #make a recursive call for left subtree
        left = self.rec(st, mid-1)

        #create the root
        root = TreeNode(self.head.val)
        self.head = self.head.next
        root.left = left

        #make a recursive call for right subtree
        root.right = self.rec(mid+1, end)

        return root
        

# @lc code=end