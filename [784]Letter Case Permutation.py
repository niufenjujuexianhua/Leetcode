# Given a string S, we can transform every letter individually to be lowercase o
# r uppercase to create another string. 
# 
#  Return a list of all possible strings we could create. You can return the out
# put in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: S = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
#  
# 
#  Example 2: 
# 
#  
# Input: S = "3z4"
# Output: ["3z4","3Z4"]
#  
# 
#  Example 3: 
# 
#  
# Input: S = "12345"
# Output: ["12345"]
#  
# 
#  Example 4: 
# 
#  
# Input: S = "0"
# Output: ["0"]
#  
# 
#  
#  Constraints: 
# 
#  
#  S will be a string with length between 1 and 12. 
#  S will consist only of letters or digits. 
#  
#  Related Topics Backtracking Bit Manipulation 
#  👍 1680 👎 114


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        self.bt(S, 0, '', res)
        return res

    def bt(self, strs, i, path, res):
        if len(path) == len(strs):
            res.append(path)
            return

        if strs[i].isdigit():
            self.bt(strs, i + 1, path + strs[i], res)
        else:
            self.bt(strs, i + 1, path + strs[i].upper(), res)
            self.bt(strs, i + 1, path + strs[i].lower(), res)
# leetcode submit region end(Prohibit modification and deletion)
