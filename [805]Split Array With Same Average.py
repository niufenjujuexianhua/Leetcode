# In a given integer array A, we must move every element of A to either list B o
# r list C. (B and C initially start empty.) 
# 
#  Return true if and only if after such a move, it is possible that the average
#  value of B is equal to the average value of C, and B and C are both non-empty. 
# 
# 
#  
# Example :
# Input: 
# [1,2,3,4,5,6,7,8]
# Output: true
# Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of 
# them have the average of 4.5.
#  
# 
#  Note: 
# 
#  
#  The length of A will be in the range [1, 30]. 
#  A[i] will be in the range of [0, 10000]. 
#  
# 
#  
#  Related Topics Math 
#  👍 446 👎 84


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A.sort()
        s = sum(A)
        n = len(A)
#         s / n = subset / cnt -> s * cnt = subset * n

        for cnt in range(1, n // 2 + 1):
            if (s * cnt) % n == 0:
                if self.dfs(A, cnt, (s * cnt) // n, 0):
                    return True
        return False

    def dfs(self, A, cnt, subset, i):
        if cnt == subset == 0:
            return True
        if cnt < 0 or subset < 0:
            return False

        for j in range(i, len(A)):
            if j > i and A[i] == A[j]: continue
            if self.dfs(A, cnt - 1, subset - A[j], j + 1):
                return True
        return False
# print(Solution().splitArraySameAverage([1,3]))
# print(Solution().splitArraySameAverage([5,3,11,19,2] ))




        
# leetcode submit region end(Prohibit modification and deletion)
