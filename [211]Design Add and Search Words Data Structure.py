# Design a data structure that supports adding new words and finding if a string
#  matches any previously added string. 
# 
#  Implement the WordDictionary class: 
# 
#  
#  WordDictionary() Initializes the object. 
#  void addWord(word) Adds word to the data structure, it can be matched later. 
# 
#  bool search(word) Returns true if there is any string in the data structure t
# hat matches word or false otherwise. word may contain dots '.' where dots can be
#  matched with any letter. 
#  
# 
#  
#  Example: 
# 
#  
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","se
# arch"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
# 
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= word.length <= 500 
#  word in addWord consists lower-case English letters. 
#  word in search consist of '.' or lower-case English letters. 
#  At most 50000 calls will be made to addWord and search. 
#  
#  Related Topics Backtracking Depth-first Search Design Trie 
#  👍 2758 👎 121


# leetcode submit region begin(Prohibit modification and deletion)
class Node():
    def __init__(self):
        self.kids = {}
        self.end = False

class WordDictionary(object):
    def __init__(self):
        self.trie = Node()

    def addWord(self, word):
        p = self.trie
        for c in word:
            if c not in p.kids:
                p.kids[c] = Node()
            p = p.kids[c]
        p.end = True

    def search(self, word):
        p = self.trie
        return self._search(p, word, 0)

    def _search(self, trie, word, i):
        if i == len(word):
            return trie.end
        if not trie.kids or (word[i] != '.' and word[i] not in trie.kids):
            return False

        if word[i] != '.':
            return self._search(trie.kids[word[i]], word, i + 1)
        else:
            return any(self._search(trie.kids[node], word, i + 1) for node in trie.kids)


# wordDictionary = WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad");
# wordDictionary.search("bad");
# wordDictionary.search(".ad");
# wordDictionary.search("b..");

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# leetcode submit region end(Prohibit modification and deletion)
