# Given an array A of 0s and 1s, we may change up to K values from 0 to 1. 
# 
#  Return the length of the longest (contiguous) subarray that contains only 1s.
#  
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation: 
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined. 
# 
# 
#  
#  Example 2: 
# 
#  
# Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Output: 10
# Explanation: 
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 20000 
#  0 <= K <= A.length 
#  A[i] is 0 or 1 
#  
#  
#  Related Topics Two Pointers Sliding Window 
#  👍 1673 👎 29


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        i, cnt, res = 0, 0, 0

        for j, a in enumerate(A):
            cnt += int(a == 0)
            while cnt > K:
                cnt -= int(A[i] == 0)
                i += 1
            res = max(res, j - i + 1)
        return res


        
# leetcode submit region end(Prohibit modification and deletion)
