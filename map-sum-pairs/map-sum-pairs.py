class Node():
    def __init__(self):
        self.node = collections.defaultdict(Node)
        self.word = False
        self.val = 0

class MapSum(object):
    def __init__(self):
        self.root = Node()
        self.dt = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        diff = val - self.dt.get(key, 0)
        self.dt[key] = val 
        p = self.root
        for ch in key:
            p = p.node[ch]
            p.val += diff 

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        p = self.root
        for ch in prefix:
            if ch not in p.node:
                return 0 
            p = p.node[ch]
        return p.val 