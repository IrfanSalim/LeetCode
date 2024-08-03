#
# @lc app=leetcode id=105 lang=python
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        inMap = {val: i for i, val in enumerate(inorder)}
        
        def build(preorder, psi, pei, inorder, isi, iei):
            if psi > pei or isi > iei:
                return None
            if psi == pei:
                return TreeNode(preorder[psi])
            idx = inMap[preorder[psi]]

            root = TreeNode(preorder[psi])
            root.left = build(preorder, psi+1, psi+(idx-isi), inorder, isi, idx-1)
            root.right = build(preorder, psi+(idx-isi) + 1, pei, inorder, idx+1, iei)

            return root
        
        n = len(preorder)
        return build(preorder, 0, n-1, inorder, 0, n-1)
        

    # def buildTree(self, A, B):
    #     if not A or not B:
    #         return None

    #     root_val = A[0]
    #     root = TreeNode(root_val)

    #     # find the index of the root in the inorder traversal
    #     root_idx = B.index(root_val)

    #     # recursively construct the left and right subtrees
    #     root.left = self.buildTree(A[1:root_idx+1], B[:root_idx])
    #     root.right = self.buildTree(A[root_idx+1:], B[root_idx+1:])

    #     return root
# @lc code=end

