# Design a special dictionary which has some words and allows you to search the 
# words in it by a prefix and a suffix. 
# 
#  Implement the WordFilter class: 
# 
#  
#  WordFilter(string[] words) Initializes the object with the words in the dicti
# onary. 
#  f(string prefix, string suffix) Returns the index of the word in the dictiona
# ry which has the prefix prefix and the suffix suffix. If there is more than one 
# valid index, return the largest of them. If there is no such word in the diction
# ary, return -1. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["WordFilter", "f"]
# [[["apple"]], ["a", "e"]]
# Output
# [null, 0]
# 
# Explanation
# WordFilter wordFilter = new WordFilter(["apple"]);
# wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = 
# "a" and suffix = 'e".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= words.length <= 15000 
#  1 <= words[i].length <= 10 
#  1 <= prefix.length, suffix.length <= 10 
#  words[i], prefix and suffix consist of lower-case English letters only. 
#  At most 15000 calls will be made to the function f. 
#  
#  Related Topics Trie 
#  👍 451 👎 225


# leetcode submit region begin(Prohibit modification and deletion)
class WordFilter(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        import collections
        self.p = collections.defaultdict(int)
        self.s = collections.defaultdict(int)
        self.dt = {}
        for j, word in enumerate(words):
            # self.dt[word] = i
            for i in range(len(word) + 1):
                pref, suff = word[0:i], word[i : len(word)]
                self.p[pref] = max(self.p[pref], j)
                self.s[suff] = max(self.s[suff], j)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        res = -1
        if self.p[prefix] == self.s[suffix]:
        if cand: return cand
        return res


        
wf = WordFilter(["apple"])
print(wf.f('a', 'e'))

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
# leetcode submit region end(Prohibit modification and deletion)
