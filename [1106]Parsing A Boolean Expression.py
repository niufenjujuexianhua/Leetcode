# Return the result of evaluating a given boolean expression, represented as a s
# tring. 
# 
#  An expression can either be: 
# 
#  
#  "t", evaluating to True; 
#  "f", evaluating to False; 
#  "!(expr)", evaluating to the logical NOT of the inner expression expr; 
#  "&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner expres
# sions expr1, expr2, ...; 
#  "|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner express
# ions expr1, expr2, ... 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: expression = "!(f)"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: expression = "|(f,t)"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: expression = "&(t,f)"
# Output: false
#  
# 
#  Example 4: 
# 
#  
# Input: expression = "|(&(t,f,t),!(t))"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= expression.length <= 20000 
#  expression[i] consists of characters in {'(', ')', '&', '|', '!', 't', 'f', '
# ,'}. 
#  expression is a valid expression representing a boolean, as given in the desc
# ription. 
#  
#  Related Topics String 
#  👍 304 👎 19


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        stack = []
        for c in expression:
            if c == ')':
                seen = set()
                while stack[-1] != '(':
                    seen.add(stack.pop())
                stack.pop()
                operator = stack.pop()
                stack.append(all(seen) if operator == '&' else any(seen) if operator == '|' else not seen.pop())
            elif c != ',':
                stack.append(True if c == 't' else False if c == 'f' else c)
        return stack.pop()

print(Solution().parseBoolExpr("|(f,&(t,t))"))




        
# leetcode submit region end(Prohibit modification and deletion)
