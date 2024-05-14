#
# @lc app=leetcode id=113 lang=python
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        ans = []
        self.getPath(root, ans, [], targetSum)
        return ans
        
    def getPath(self, root, ans, curr, target):
        if not root:
            return
        curr.append(root.val)
        if not root.right and not root.left and root.val == target:
            ans.append(curr[:])
        else:
            self.getPath(root.left, ans, curr, target - root.val)
            self.getPath(root.right, ans, curr, target - root.val)
        curr.pop()
# @lc code=end

