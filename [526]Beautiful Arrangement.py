# Suppose you have n integers labeled 1 through n. A permutation of those n inte
# gers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <=
#  i <= n), either of the following is true: 
# 
#  
#  perm[i] is divisible by i. 
#  i is divisible by perm[i]. 
#  
# 
#  Given an integer n, return the number of the beautiful arrangements that you 
# can construct. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: 2
# Explanation: 
# The first beautiful arrangement is [1,2]:
#     - perm[1] = 1 is divisible by i = 1
#     - perm[2] = 2 is divisible by i = 2
# The second beautiful arrangement is [2,1]:
#     - perm[1] = 2 is divisible by i = 1
#     - i = 2 is divisible by perm[2] = 1
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 15 
#  
#  Related Topics Backtracking Depth-first Search 
#  👍 1142 👎 201


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = self.bt(n, 0, 0, {})
        return res

    def bt(self, n, cnt, used, memo):
        if cnt == n:
            return 1
        if used in memo:
            return memo[used]

        res = 0
        for i in range(1, n + 1):
            size = cnt + 1
            if not used & (1 << (i - 1)) and (size % i == 0 or i % size == 0):
                res += self.bt(n, cnt + 1, used | (1 << (i - 1)), memo)
        memo[used] = res
        return res

# print(Solution().countArrangement(1))
# print(Solution().countArrangement(2))
# print(Solution().countArrangement(3))
# print(Solution().countArrangement(7))

# leetcode submit region end(Prohibit modification and deletion)
