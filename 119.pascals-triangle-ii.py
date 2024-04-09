#
# @lc app=leetcode id=119 lang=python
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev_row = [1]
        for i in range(1, rowIndex + 1):
            new_row = [1]
            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])
            new_row.append(1)
            prev_row = new_row
        
        return prev_row

        # pascal = [[1]]
        # for i in range(1, rowIndex + 1):
        #     prev_row = pascal[-1]
        #     new_row = [1]
        #     for j in range(1, i):
        #         new_row.append(prev_row[j - 1] + prev_row[j])
        #     new_row.append(1)
        #     pascal.append(new_row)
        
        # return pascal[-1]

# @lc code=end

