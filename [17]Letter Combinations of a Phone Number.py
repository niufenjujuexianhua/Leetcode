# Given a string containing digits from 2-9 inclusive, return all possible lette
# r combinations that the number could represent. Return the answer in any order. 
# 
# 
#  A mapping of digit to letters (just like on the telephone buttons) is given b
# elow. Note that 1 does not map to any letters. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#  
# 
#  Example 2: 
# 
#  
# Input: digits = ""
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: digits = "2"
# Output: ["a","b","c"]
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= digits.length <= 4 
#  digits[i] is a digit in the range ['2', '9']. 
#  
#  Related Topics String Backtracking Depth-first Search Recursion 
#  👍 5276 👎 488


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []

        dt = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        self.bt(dt, digits, 0, '', res)
        return res

    def bt(self, dt, digits, i, path, res):
        if i == len(digits):
            res.append(path)
            return

        for let in dt[digits[i]]:
            self.bt(dt, digits, i + 1, path + let, res)
        
# leetcode submit region end(Prohibit modification and deletion)
