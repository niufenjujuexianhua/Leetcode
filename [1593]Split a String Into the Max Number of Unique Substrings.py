# Given a string s, return the maximum number of unique substrings that the give
# n string can be split into. 
# 
#  You can split string s into any list of non-empty substrings, where the conca
# tenation of the substrings forms the original string. However, you must split th
# e substrings such that all of them are unique. 
# 
#  A substring is a contiguous sequence of characters within a string. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "ababccc"
# Output: 5
# Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitt
# ing like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' mu
# ltiple times.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "aba"
# Output: 2
# Explanation: One way to split maximally is ['a', 'ba'].
#  
# 
#  Example 3: 
# 
#  
# Input: s = "aa"
# Output: 1
# Explanation: It is impossible to split the string any further.
#  
# 
#  
#  Constraints: 
# 
#  
#  
#  1 <= s.length <= 16 
#  
#  
#  s contains only lower case English letters. 
#  
#  
#  Related Topics Backtracking 
#  👍 229 👎 11


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.res = 0
        self.dfs(s, 0, set())
        return self.res

    def dfs(self, s, i, path):
        if i == len(s):
            self.res = max(self.res, len(path))
            return

        for j in range(i, len(s)):
            subs = s[i:j + 1]
            if subs not in path and len(path) + len(s) - j > self.res:
                path.add(subs)
                self.dfs(s, j + 1, path)
                path.remove(subs)
        
# leetcode submit region end(Prohibit modification and deletion)
