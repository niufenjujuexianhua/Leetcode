# Given two words (beginWord and endWord), and a dictionary's word list, find al
# l shortest transformation sequence(s) from beginWord to endWord, such that: 
# 
#  
#  Only one letter can be changed at a time 
#  Each transformed word must exist in the word list. Note that beginWord is not
#  a transformed word. 
#  
# 
#  Note: 
# 
#  
#  Return an empty list if there is no such transformation sequence. 
#  All words have the same length. 
#  All words contain only lowercase alphabetic characters. 
#  You may assume no duplicates in the word list. 
#  You may assume beginWord and endWord are non-empty and are not the same. 
#  
# 
#  Example 1: 
# 
#  
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
#  
# 
#  Example 2: 
# 
#  
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# Output: []
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible trans
# formation.
#  
# 
#  
#  
#  Related Topics Array String Backtracking Breadth-first Search 
#  👍 2098 👎 266


# leetcode submit region begin(Prohibit modification and deletion)
import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return []

        all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        dq = collections.deque([[beginWord, [beginWord]]])
        seen = set([beginWord])
        res = []

        while dq:
            size = len(dq)
            localseen = set()
            for _ in range(size):
                word, path = dq.popleft()

                if word == endWord:
                    res.append(path)

                for i in range(len(word)):
                    for newword in all_combo_dict[word[:i] + '*' + word[i+1:]]:
                        if newword not in seen and newword in wordList:
                            localseen.add(newword)
                            dq.append([newword, path + [newword]])
            seen = seen.union(localseen)
            if res:
                break

        return res
# "hit","hot","lot","log","cog"
# print(Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
        
# leetcode submit region end(Prohibit modification and deletion)
