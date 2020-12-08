# Implement a basic calculator to evaluate a simple expression string. 
# 
#  The expression string may contain open ( and closing parentheses ), the plus 
# + or minus sign -, non-negative integers and empty spaces . 
# 
#  Example 1: 
# 
#  
# Input: "1 + 1"
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: " 2-1 + 2 "
# Output: 3 
# 
#  Example 3: 
# 
#  
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23 
# Note:
# 
#  
#  You may assume that the given expression is always valid. 
#  Do not use the eval built-in library function. 
#  
#  Related Topics Math Stack 
#  👍 1828 👎 143


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        (1+
            (4+5+2)-3)+(6+8)
        """
        st = []
        sign = 1
        res = 0
        n = 0
        for c in s:
            if c == ' ':
                continue
            elif c in ['+', '-']:
                res += n * sign
                n = 0
                sign = [-1, 1][c == '+']
            elif c.isdigit():
                n = n * 10 + int(c)
            elif c == '(':
                st.append(res)
                st.append(sign)
                res, sign = 0, 1
            elif c == ')':
                res += sign * n
                n, sign = 0, 1
                res *= st.pop()
                res += st.pop()
        return res + sign * n

# print(Solution().calculate(" 2-1 + 2 "))

        
# leetcode submit region end(Prohibit modification and deletion)
