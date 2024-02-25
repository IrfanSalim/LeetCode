#
# @lc app=leetcode id=230 lang=python
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        #optimal approach with morris inorder traversal
        #no space used
        curr = root
        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                temp = curr.left
                while temp.right and temp.right != curr:
                    temp = temp.right
                if not temp.right:
                    temp.right = curr
                    curr = curr.left
                else:
                    temp.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right

        #dfs approach to traverse inorder and find kth number
        #approach will take O(height) space
        # count = [0]
        # ans = [0]
        # def dfs(A, k):
        #     if not A:
        #         return
        #     dfs(A.left, k)
        #     count[0] += 1
        #     if count[0] == k:
        #         ans[0] = A.val
        #     dfs(A.right, k)
        # dfs(root, k)
        # return ans[0]
# @lc code=end

