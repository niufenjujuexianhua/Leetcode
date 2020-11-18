# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of 
# s1 and s2. 
# 
#  An interleaving of two strings s and t is a configuration where they are divi
# ded into non-empty substrings such that: 
# 
#  
#  s = s1 + s2 + ... + sn 
#  t = t1 + t2 + ... + tm 
#  |n - m| <= 1 
#  The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + 
# t3 + s3 + ... 
#  
# 
#  Note: a + b is the concatenation of strings a and b. 
# 
#  
#  Example 1: 
# 
#  
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: s1 = "", s2 = "", s3 = ""
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s1.length, s2.length <= 100 
#  0 <= s3.length <= 200 
#  s1, s2, and s3 consist of lower-case English letters. 
#  
#  Related Topics String Dynamic Programming 
#  👍 1712 👎 97


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        if m + n != len(s3): return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            if dp[i - 1][0] and s1[i - 1] == s3[i - 1]:
                dp[i][0] = True

        for j in range(1, n + 1):
            if dp[0][j - 1] and s2[j - 1] == s3[j - 1]:
                dp[0][j] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = True
                elif dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1]

# leetcode submit region end(Prohibit modification and deletion)
