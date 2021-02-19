# Given a string s, partition s such that every substring of the partition is a 
# palindrome. Return all possible palindrome partitioning of s. 
# 
#  A palindrome string is a string that reads the same backward as forward. 
# 
#  
#  Example 1: 
#  Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
#  Example 2: 
#  Input: s = "a"
# Output: [["a"]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 16 
#  s contains only lowercase English letters. 
#  
#  Related Topics Dynamic Programming Backtracking Depth-first Search 
#  👍 3017 👎 97


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.bt(s, 0, [], res)
        return res

    def bt(self, s, i, path, res):
        if i == len(s):
            res.append(path)
            return

        for j in range(i, len(s)):
            subs = s[i:j + 1]
            if subs == subs[::-1]:
                self.bt(s, j + 1, path + [subs], res)

# print(Solution().partition('a'))
# leetcode submit region end(Prohibit modification and deletion)
