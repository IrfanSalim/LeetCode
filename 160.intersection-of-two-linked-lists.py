#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1, l2 = headA, headB
        # the short but non intuitive hard to read solution
        # while l1 != l2:
        #     l1 = l1.next if l1 else headB
        #     l2 = l2.next if l2 else headA
        # return l1

        #easy to understand solution
        #calculate the len of both list 
        lenA, lenB = 0, 0
        while l1:
            lenA += 1
            l1 = l1.next
        while l2:
            lenB += 1
            l2 = l2.next

        #move the longer one ahead by difference 
        l1, l2 = headA, headB
        for i in range(abs(lenA - lenB)):
            if lenA > lenB:
                l1 = l1.next
            else:
                l2 = l2.next
        
        #and then check for equal nodes until end
        while l1 and l2:
            if l1 == l2:
                return l1
            l1 = l1.next
            l2 = l2.next
        return None

# @lc code=end

