#
# @lc app=leetcode id=92 lang=python
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right:
            return head
        # create a dummy node to handle edge cases
        dummy = ListNode(0, head)

        #assign a variable to the node just before left and find left
        first, curr = dummy, head
        for i in range(left - 1):
            first, curr = curr, curr.next

        #reverse the list from left to right
        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        
        #connect the reversed list to original list
        first.next.next = curr
        first.next = prev
        return dummy.next
# @lc code=end

