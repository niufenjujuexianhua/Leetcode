# A transformation sequence from word beginWord to word endWord using a dictiona
# ry wordList is a sequence of words such that: 
# 
#  
#  The first word in the sequence is beginWord. 
#  The last word in the sequence is endWord. 
#  Only one letter is different between each adjacent pair of words in the seque
# nce. 
#  Every word in the sequence is in wordList. 
#  
# 
#  Given two words, beginWord and endWord, and a dictionary wordList, return the
#  number of words in the shortest transformation sequence from beginWord to endWo
# rd, or 0 if no such sequence exists. 
# 
#  
#  Example 1: 
# 
#  
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot"
# ,"log","cog"]
# Output: 5
# Explanation: One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -
# > "cog" with 5 words.
#  
# 
#  Example 2: 
# 
#  
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot"
# ,"log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no possi
# ble transformation.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= beginWord.length <= 10 
#  endWord.length == beginWord.length 
#  1 <= wordList.length <= 5000 
#  wordList[i].length == beginWord.length 
#  beginWord, endWord, and wordList[i] consist of lowercase English letters. 
#  beginWord != endWord 
#  All the strings in wordList are unique. 
#  
#  Related Topics Breadth-first Search 
#  👍 4592 👎 1388


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList: return 0

        dt = self.prepro(wordList)
        f, b = set([beginWord]), set([endWord])
        seen = set([beginWord, endWord])
        step = 1

        while f and b:
            nlevel = set()
            if len(f) > len(b):
                f, b = b, f
            while f:
                word = f.pop()
                for i in range(len(word)):
                    for nxt in dt[word[:i] + '_' + word[i + 1:]]:
                        if nxt in b:
                            return step + 1
                        if nxt not in seen:
                            seen.add(nxt)
                            nlevel.add(nxt)
            step += 1
            f = nlevel
        return 0

    def prepro(self, wordlist):
        import collections
        dt = collections.defaultdict(set)
        for word in wordlist:
            for i in range(len(word)):
                dt[word[:i] + '_' + word[i + 1:]].add(word)
        return dt
print(Solution().ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
        
# leetcode submit region end(Prohibit modification and deletion)
