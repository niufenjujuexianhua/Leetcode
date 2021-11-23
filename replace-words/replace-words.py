class Node():
    def __init__(self):
        self.node = collections.defaultdict(Node)
        self.end = False
        self.word = None 

class Trie():
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        p = self.root 
        for ch in word:
            p = p.node[ch]
        p.end = True
        p.word = word 
    
    def search(self, word):
        p = self.root
        for ch in word:
            if ch not in p.node:
                return word 
            p = p.node[ch]
            if p.end:
                return p.word 
        return word 
        

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for prefix in dictionary:
            trie.insert(prefix)
            
        res = [] 
        words = sentence.split(' ')
        for word in words:
            res.append(trie.search(word))
        
        return ' '.join(res)