#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        dummy = head
        carry = 0
        while l1 or l2:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = sum // 10
            dummy.val = sum % 10
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            if l1 or l2 or carry:
                dummy.next = ListNode(0)
                dummy = dummy.next
            
            if carry:
                dummy.val = carry
                
        return head

# @lc code=end

