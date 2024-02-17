#
# @lc app=leetcode id=108 lang=python
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        s = 0
        e = len(nums) - 1
        def create(A, s, e):
            if s > e:
                return
            m = (s + e)//2
            root = TreeNode(A[m])
            root.left = create(A, s, m - 1)
            root.right = create(A, m + 1, e)
            return root
        return create(nums, s, e)        
# @lc code=end

