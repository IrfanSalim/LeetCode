#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        #recursive function to make all permutations
        def backtrack(ans, arr, A, used):
            if len(arr) == len(A):
                ans.append(arr[:])
                return
            for i in range(len(A)):
                if not used[i]:
                    used[i] = True
                    arr.append(A[i])
                    backtrack(ans, arr, A, used)
                    used[i] = False
                    arr.pop()
        #call the function
        backtrack(ans, [], nums, [False] * len(nums))
        return ans
        
# @lc code=end

