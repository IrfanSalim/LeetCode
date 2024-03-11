#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for i, head in enumerate(lists):
            if head: 
                heapq.heappush(heap, (head.val, i, head))

        dummy = curr = ListNode(0)
        while heap:
            val, i, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
            curr.next = node
            curr = curr.next
        
        return dummy.next
# @lc code=end

