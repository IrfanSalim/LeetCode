#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # approach with a single pass
        dummy = ListNode(0, head)
        curr = temp = dummy
        # move the curr ahead n times
        for i in range(n):
            curr = curr.next
            
        # move temp and head together until curr reaches end
        while curr.next:
            curr = curr.next
            temp = temp.next
        
        #remove nth node
        temp.next = temp.next.next
        return dummy.next

        # this approach required two passes on the LL
        # curr = head
        # size = 0

        # #get the size of the linked list
        # while curr:
        #     size += 1
        #     curr = curr.next

        # #edge case   
        # if size == 1 and n > 0:
        #     return None
        # if n >= size:
        #     head = head.next
        #     return head
        
        # curr = head
        # #iterate to the node prior to the nth node from end
        # for _ in range(size - n - 1):
        #     curr = curr.next
        
        # #delete the nth node by removing the connection
        # curr.next = curr.next.next
        # return head
# @lc code=end

