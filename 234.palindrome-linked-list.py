#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #find the middle node
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #reverse the list from middle onwards
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        #compare both the ends
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
        
# @lc code=end

