# Given a non-empty string s and a dictionary wordDict containing a list of non-
# empty words, add spaces in s to construct a sentence where each word is a valid 
# dictionary word. Return all such possible sentences. 
# 
#  Note: 
# 
#  
#  The same word in the dictionary may be reused multiple times in the segmentat
# ion. 
#  You may assume the dictionary does not contain duplicate words. 
#  
# 
#  Example 1: 
# 
#  
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
#  
# 
#  Example 2: 
# 
#  
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
#  
# 
#  Example 3: 
# 
#  
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# [] 
#  Related Topics Dynamic Programming Backtracking 
#  👍 2887 👎 441


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        dp = self.breakable(s, wordDict)
        if not dp[-1]:
            return []

        res = []
        size = max([len(word) for word in wordDict])
        self.dfs(s, wordDict, 0, dp, '', res, size)
        return res

    def dfs(self, s, wordDict, pos, dp, path, res, size):
        if pos == len(s):
            res.append(path.strip())
            return

        for i in range(pos, min(pos + size + 1, len(dp))):
            if dp[i] == 1:
                word = s[pos:i]
                if word in wordDict:
                    self.dfs(s, wordDict, i, dp, path + ' ' + word, res, size)

        # for word in wordDict:
        #     if s.startswith(word):
        #         self.dfs(s[len(word):], wordDict, path + ' ' + word, res)

    def breakable(self, s, wordDict):
        dp = [1] + [0] * len(s)
        for j in range(len(s)):
            for i in range(j + 1):
                if dp[i] and s[i:j + 1] in wordDict:
                    dp[j + 1] = 1
        return dp
# print(Solution().wordBreak('a', ['b']))
# leetcode submit region end(Prohibit modification and deletion)
