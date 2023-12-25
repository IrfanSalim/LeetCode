#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n, m = len(nums1), len(nums2)
        l, h = 0, n
        inf = float('inf')
        _inf = float('-inf')
        while l <= h:
            cut1 = l + (h-l)//2
            cut2 = (n+m+1)//2 - cut1
            l1 = _inf if cut1 == 0 else nums1[cut1-1]
            l2 = _inf if cut2 == 0 else nums2[cut2-1]
            r1 = inf if cut1 == n else nums1[cut1]
            r2 = inf if cut2 == m else nums2[cut2]
            if l1<=r2 and l2<=r1:
                if (n+m) % 2 == 0:
                    return (float(max(l1, l2)) + float(min(r1, r2)))/2
                else:
                    return max(l1, l2)
            elif l1 > r2:
                h = cut1 - 1
            else:
                l = cut1 + 1
        
# @lc code=end

