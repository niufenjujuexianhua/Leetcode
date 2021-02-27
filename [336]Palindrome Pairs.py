# Given a list of unique words, return all the pairs of the distinct indices (i,
#  j) in the given list, so that the concatenation of the two words words[i] + wor
# ds[j] is a palindrome. 
# 
#  
#  Example 1: 
# 
#  
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
#  
# 
#  Example 2: 
# 
#  
# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
#  
# 
#  Example 3: 
# 
#  
# Input: words = ["a",""]
# Output: [[0,1],[1,0]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= words.length <= 5000 
#  0 <= words[i].length <= 300 
#  words[i] consists of lower-case English letters. 
#  
#  Related Topics Hash Table String Trie 
#  👍 1688 👎 165


# leetcode submit region begin(Prohibit modification and deletion)
class Trie():
    def __init__(self):
        self.idx = -1
        self.ls = []
        self.node = {}

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        trie = Trie()
        for i, word in enumerate(words):
            self.insert(trie, word, i)

        res = []
        for i, word in enumerate(words):
            self.search(trie, word, i, res)
        return res

    def insert(self, trie, word, k):
        for j in reversed(range(len(word))):
            if word[j] not in trie.node:
                trie.node[word[j]] = Trie()

            if self.isPal(word, 0, j):
                trie.ls.append(k)
            trie = trie.node[word[j]]
        trie.ls.append(k)
        trie.idx = k

    def search(self, trie, word, k, res):
        for i in range(len(word)):
            if trie.idx != -1 and trie.idx != k and self.isPal(word, i, len(word) - 1):
                res.append([k, trie.idx])
            if word[i] in trie.node:
                trie = trie.node[word[i]]
            else:
                return
        for idx in trie.ls:
            if idx != k:
                res.append([k, idx])

    def isPal(self, word, i, j):
        while i < j:
            if word[i] != word[j]: return False
            i += 1
            j -= 1
        return True

# print(Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]))
# print(Solution().palindromePairs(["bat","tab","cat"]))
print(Solution().palindromePairs(["a",""]))
# print(Solution().palindromePairs(["a","abc","aba",""]))
# leetcode submit region end(Prohibit modification and deletion)
