#
# @lc app=leetcode id=239 lang=python
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque()
        ans = []
        for i in range(k):
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
        ans.append(q[0])
        st, end = 0, k
        while end < len(nums):
            if q[0] == nums[st]:
                q.popleft()
            while q and nums[end] > q[-1]:
                q.pop()
            q.append(nums[end])
            ans.append(q[0])
            st += 1
            end += 1
        return ans
            
# @lc code=end

