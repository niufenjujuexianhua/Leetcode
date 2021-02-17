# Given n pairs of parentheses, write a function to generate all combinations of
#  well-formed parentheses. 
# 
#  
#  Example 1: 
#  Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
#  Example 2: 
#  Input: n = 1
# Output: ["()"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= n <= 8 
#  
#  Related Topics String Backtracking 
#  👍 7118 👎 312


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.bt(0, 0, n, '', res)
        return res

    def bt(self, lt, rt, n, path, res):
        if lt > n or rt > n or rt > lt:
            return
        if len(path) == 2 * n:
            res.append(path)
            return

        self.bt(lt + 1, rt, n, path + '(', res)
        self.bt(lt, rt + 1, n, path + ')', res)

        
# leetcode submit region end(Prohibit modification and deletion)
