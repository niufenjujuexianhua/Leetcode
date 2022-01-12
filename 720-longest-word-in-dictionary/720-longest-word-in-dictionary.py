import collections
class Node():
    def __init__(self):
        self.child = collections.defaultdict(Node)
        self.end = False

class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, w):
        p = self.root
        for ch in w:
            p = p.child[ch]
        p.end = True

    def search(self, w):
        p = self.root
        for ch in w:
            if ch not in p.child:
                return False
            if not p.child[ch].end:
                return False
            p = p.child[ch]
        return p.end



class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        trie = Trie()
        for w in words:
            trie.insert(w)

        words = sorted(words, key = lambda w : (-len(w), w))
        for w in words:
            if trie.search(w):
                return w
        return ''