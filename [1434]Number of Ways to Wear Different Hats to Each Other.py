# There are n people and 40 types of hats labeled from 1 to 40. 
# 
#  Given a list of list of integers hats, where hats[i] is a list of all hats pr
# eferred by the i-th person. 
# 
#  Return the number of ways that the n people wear different hats to each other
# . 
# 
#  Since the answer may be too large, return it modulo 10^9 + 7. 
# 
#  
#  Example 1: 
# 
#  
# Input: hats = [[3,4],[4,5],[5]]
# Output: 1
# Explanation: There is only one way to choose hats given the conditions. 
# First person choose hat 3, Second person choose hat 4 and last one hat 5. 
# 
#  Example 2: 
# 
#  
# Input: hats = [[3,5,1],[3,5]]
# Output: 4
# Explanation: There are 4 ways to choose hats
# (3,5), (5,3), (1,3) and (1,5)
#  
# 
#  Example 3: 
# 
#  
# Input: hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# Output: 24
# Explanation: Each person can choose hats labeled from 1 to 4.
# Number of Permutations of (1,2,3,4) = 24.
#  
# 
#  Example 4: 
# 
#  
# Input: hats = [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]
# Output: 111
#  
# 
#  
#  Constraints: 
# 
#  
#  n == hats.length 
#  1 <= n <= 10 
#  1 <= hats[i].length <= 40 
#  1 <= hats[i][j] <= 40 
#  hats[i] contains a list of unique integers. 
#  Related Topics Dynamic Programming Bit Manipulation 
#  👍 324 👎 3


# leetcode submit region begin(Prohibit modification and deletion)
import collections
class Solution(object):

    def numberWays(self, hats):
        """
        :type hats: List[List[int]]
        :rtype: int
        """
        n = len(hats)
        dp = [0] * (1 << n)
        dp[0] = 1
        m = 1e9+7

        per2hat = collections.defaultdict(set)
        for per in range(n):
            for hat in hats[per]:
                per2hat[hat].add(per)

        for hat in range(1, 41):
            dp_new = dp[:]
            for state in range((1 << n)):
                for per in per2hat[hat]:
                    if (state >> (n - per - 1)) & 1:
                        continue
                    pstate = 1 << (n - per - 1)
                    dp_new[state | pstate] += dp[state]
                    dp_new[state | pstate] %= m
            dp = dp_new

        return int(dp[(1 << n) - 1])

# print(Solution().numberWays([[3,4],[4,5],[5]]))
# leetcode submit region end(Prohibit modification and deletion)
