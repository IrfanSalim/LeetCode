#
# @lc app=leetcode id=43 lang=python
#
# [43] Multiply Strings
#

# @lc code=start
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        N = len(num1) + len(num2)
        res = [0] * N       
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                val = int(num1[i]) * int(num2[j])
                p1,p2 = i+j,i+j+1
                sum = val + res[p2]
                res[p2] = sum % 10
                res[p1] += sum // 10
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        res_str = ''.join(str(e) for e in res[i:])        
        return res_str if res_str else '0'      
# @lc code=end

