# You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and
#  'R'. 
# 
#  A string is said to be balanced if each of its characters appears n/4 times w
# here n is the length of the string. 
# 
#  Return the minimum length of the substring that can be replaced with any othe
# r string of the same length to make the original string s balanced. 
# 
#  Return 0 if the string is already balanced. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "QWER"
# Output: 0
# Explanation: s is already balanced. 
# 
#  Example 2: 
# 
#  
# Input: s = "QQWE"
# Output: 1
# Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is ba
# lanced.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "QQQW"
# Output: 2
# Explanation: We can replace the first "QQ" to "ER". 
#  
# 
#  Example 4: 
# 
#  
# Input: s = "QQQQ"
# Output: 3
# Explanation: We can replace the last 3 'Q' to make s = "QWER".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10^5 
#  s.length is a multiple of 4 
#  s contains only 'Q', 'W', 'E' and 'R'. 
#  
#  Related Topics Two Pointers String 
#  👍 475 👎 103


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        dt = collections.Counter(s)
        n = res = len(s)
        i = 0
        for j, c in enumerate(s):
            dt[c] -= 1

            while i < n and all(c <= n // 4 for c in dt.values()):
                res = min(res, j - i + 1)
                dt[s[i]] += 1
                i += 1
        return res

        
# leetcode submit region end(Prohibit modification and deletion)
