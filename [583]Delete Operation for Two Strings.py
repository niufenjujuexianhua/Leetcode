# 
# Given two words word1 and word2, find the minimum number of steps required to 
# make word1 and word2 the same, where in each step you can delete one character i
# n either string.
#  
# 
#  Example 1: 
#  
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make 
# "eat" to "ea".
#  
#  
# 
#  Note: 
#  
#  The length of given words won't exceed 500. 
#  Characters in given words can only be lower-case letters. 
#  
#  Related Topics String 
#  👍 1268 👎 30


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        return self.dfs(m, n, word1, word2, {})

    def dfs(self, i, j, word1, word2, memo):
        if i == 0:
            return j
        if j == 0:
            return i
        if (i, j) in memo:
            return memo[(i, j)]

        ans = float('inf')
        if word1[i -1] == word2[j - 1]:
            ans = min(ans, self.dfs(i - 1, j - 1, word1, word2, memo))
        else:
            ans = min(ans,
                      self.dfs(i, j - 1, word1, word2, memo) + 1,
                      self.dfs(i - 1, j, word1, word2, memo) + 1)

        memo[(i, j)] = ans
        return ans

        
# leetcode submit region end(Prohibit modification and deletion)
