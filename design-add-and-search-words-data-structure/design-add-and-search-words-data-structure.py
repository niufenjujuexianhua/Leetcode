class Node():
    def __init__(self):
        self.node = collections.defaultdict(Node)
        self.end = False


class WordDictionary(object):
    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        p = self.root 
        for ch in word:
            p = p.node[ch]
        p.end = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        root = self.root 
        return self._search(root, word, 0)
    
    def _search(self, root, word, i):
        if i == len(word):
            return root.end 
        
        if word[i] != '.':
            if word[i] not in root.node:
                return False
            return self._search(root.node[word[i]], word, i + 1)
        else:
            return any(self._search(root.node[ch], word, i + 1) for ch in root.node)