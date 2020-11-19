# Given two strings s1, s2, find the lowest ASCII sum of deleted characters to m
# ake two strings equal. 
# 
#  Example 1: 
#  
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the 
# sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum pos
# sible to achieve this.
#  
#  
# 
#  Example 2: 
#  
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to
#  the sum.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101
#  = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers of
#  433 or 417, which are higher.
#  
#  
# 
#  Note:
#  0 < s1.length, s2.length <= 1000. 
#  All elements of each string will have an ASCII value in [97, 122]. 
#  Related Topics Dynamic Programming 
#  👍 1123 👎 51


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        m, n = len(s1), len(s2)

        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]),
                                   dp[i][j - 1] + ord(s2[j - 1]))
        return dp[-1][-1]
        
# leetcode submit region end(Prohibit modification and deletion)
