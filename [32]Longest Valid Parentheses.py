# Given a string containing just the characters '(' and ')', find the length of 
# the longest valid (well-formed) parentheses substring. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
#  
# 
#  Example 2: 
# 
#  
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
#  
# 
#  Example 3: 
# 
#  
# Input: s = ""
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 3 * 104 
#  s[i] is '(', or ')'. 
#  
#  Related Topics String Dynamic Programming 
#  👍 4782 👎 175


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = r = res = 0
        for c in s:
            if c == '(':
                l += 1
            else:
                r += 1

            if l == r:
                res = max(res, l * 2)
            elif l < r:
                l = r = 0

        l = r = 0
        for c in reversed(s):
            if c == '(':
                l += 1
            else:
                r += 1

            if l == r:
                res = max(res, l * 2)
            elif l > r:
                l = r = 0
        return res
    # print(Solution().longestValidParentheses(")("))
# leetcode submit region end(Prohibit modification and deletion)
