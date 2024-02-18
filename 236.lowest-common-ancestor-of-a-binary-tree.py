#
# @lc app=leetcode id=236 lang=python
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


        #approach using 2 arrays to find node paths with extra space 

        # pathP = []
        # pathQ = []
        # def getPath(A, B, array):
        #     if not A:
        #         return
        #     if A == B:
        #         array.append(A)
        #         return True
        #     if getPath(A.left, B, array):
        #         array.append(A)
        #         return True
        #     if getPath(A.right, B, array):
        #         array.append(A)
        #         return True
        #     return False
        
        # getPath(root, p, pathP)
        # getPath(root, q, pathQ)

        # if not pathP or not pathQ:
        #     return None
            
        # i, j = len(pathP) - 1, len(pathQ) - 1
        
        # while i >= 0 and j >= 0 and pathP[i] == pathQ[j]:
        #     i -= 1
        #     j -= 1
        
        # return pathP[i + 1]


    #approach using recursion with less space
        
    #     if not self.find(root, p) or not self.find(root, q):
    #         return None

    #     return self.LCA(root, p, q)

    # def find(self, A, B):
    #     if not A:
    #         return False
    #     if A == B:
    #         return True
    #     lc = self.find(A.left, B)
    #     rc = self.find(A.right, B)
    #     return lc or rc
    
    # def LCA(self, A, B, C):
    #     if not A or A == B or A == C:
    #         return A
    #     left = self.LCA(A.left, B, C)
    #     right = self.LCA(A.right, B, C)
    #     if left and right:
    #         return A
    #     elif not left or not right:
    #         return left if left else right
# @lc code=end

