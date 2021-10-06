class Node(object):
    def __init__(self):
        self.dt = collections.defaultdict(Node)
        self.end = False 
        
class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root 
        for ch in word:
            cur = cur.dt[ch]
        cur.end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for ch in word:
            if ch not in cur.dt:
                return False
            cur = cur.dt[ch]
        return cur.end
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for ch in prefix:
            if ch not in cur.dt:
                return False
            cur = cur.dt[ch]
        return True

    
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
