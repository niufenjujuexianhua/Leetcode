# 
# There is a strange printer with the following two special requirements:
# 
#  
#  The printer can only print a sequence of the same character each time. 
#  At each turn, the printer can print new characters starting from and ending a
# t any places, and will cover the original existing characters. 
#  
# 
#  
# 
#  
# Given a string consists of lower English letters only, your job is to count th
# e minimum number of turns the printer needed in order to print it.
#  
# 
#  Example 1: 
#  
# Input: "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
#  
#  
# 
#  Example 2: 
#  
# Input: "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of the
#  string, which will cover the existing character 'a'.
#  
#  
# 
#  Hint: Length of the given string will not exceed 100. Related Topics Dynamic 
# Programming Depth-first Search 
#  👍 496 👎 51


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        dp = [[float('inf')] * n for _ in range(n)]

        for j in range(n):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][j] = 1
                elif i + 1 == j:
                    dp[i][j] = 1 + int(s[i] != s[j])
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j],
                                       dp[i][k] + dp[k + 1][j] - int(s[i] == s[j]))
        return dp[0][-1]

# leetcode submit region end(Prohibit modification and deletion)
