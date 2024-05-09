#
# @lc app=leetcode id=24 lang=python
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            first = curr.next
            second = first.next
            curr.next = second
            first.next = second.next
            second.next = first
            curr = curr.next.next
        return dummy.next
# @lc code=end

