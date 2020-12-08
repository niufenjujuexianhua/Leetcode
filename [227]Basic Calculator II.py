# Given a string s which represents an expression, evaluate this expression and 
# return its value. 
# 
#  The integer division should truncate toward zero. 
# 
#  
#  Example 1: 
#  Input: s = "3+2*2"
# Output: 7
#  Example 2: 
#  Input: s = " 3/2 "
# Output: 1
#  Example 3: 
#  Input: s = " 3+5 / 2 "
# Output: 5
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 3 * 105 
#  s consists of integers and operators ('+', '-', '*', '/') separated by some n
# umber of spaces. 
#  s represents a valid expression. 
#  All the integers in the expression are non-negative integers in the range [0,
#  231 - 1]. 
#  The answer is guaranteed to fit in a 32-bit integer. 
#  
#  Related Topics String Stack 
#  👍 1948 👎 316


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(self, s):
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            c = s[i]
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i]
        return sum(stack)

print(Solution().calculate('5-4*2+1'))
#     3+2*2+3
        
# leetcode submit region end(Prohibit modification and deletion)
