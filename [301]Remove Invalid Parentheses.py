# Remove the minimum number of invalid parentheses in order to make the input st
# ring valid. Return all possible results. 
# 
#  Note: The input string may contain letters other than the parentheses ( and )
# . 
# 
#  Example 1: 
# 
#  
# Input: "()())()"
# Output: ["()()()", "(())()"]
#  
# 
#  Example 2: 
# 
#  
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
#  
# 
#  Example 3: 
# 
#  
# Input: ")("
# Output: [""]
#  Related Topics Depth-first Search Breadth-first Search 
#  👍 2950 👎 133


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        lt, rt, valid = self.cnt(s)
        if valid: return [s]

        res = set()
        self.dfs(s, lt, rt, res, set())
        return list(res)

    def dfs(self, s, lt, rt, res, seen):
        if lt == rt == 0:
            _, _, valid = self.cnt(s)
            if valid:
                res.add(s)
            return

        if s in seen:
            return

        seen.add(s)
        for i in range(len(s)):
            if s[i] == '(' and lt > 0:
                self.dfs(s[:i] + s[i + 1:], lt - 1, rt, res, seen)
            elif s[i] == ')' and rt > 0:
                self.dfs(s[:i] + s[i + 1:], lt, rt - 1, res, seen)

    def cnt(self, s):
            lt = rt = 0
            for c in s:
                if c == '(':
                    lt += 1
                elif c == ')':
                    if lt >= 1:
                        lt -= 1
                    else:
                        rt += 1
            return lt, rt, lt == rt == 0
        
# leetcode submit region end(Prohibit modification and deletion)
