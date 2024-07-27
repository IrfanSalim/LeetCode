#
# @lc app=leetcode id=25 lang=python
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pointer = dummy

        while pointer:
            curr = pointer
            i = 0
            while i < k and curr:
                curr = curr.next
                i += 1
            if not curr:
                break

            prev, curr = None, pointer.next
            for i in range(k):
                next = curr.next
                curr.next = prev
                prev, curr = curr, next
            
            tail = pointer.next
            tail.next = curr
            pointer.next = prev
            pointer = tail
        
        return dummy.next
        
# @lc code=end

