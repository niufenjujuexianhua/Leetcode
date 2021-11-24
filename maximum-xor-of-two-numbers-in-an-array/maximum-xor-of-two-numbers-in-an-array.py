class Node():
    def __init__(self):
        self.node = collections.defaultdict(Node)

class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, n):
        p = self.root
        for i in range(31, -1, -1):
            bit = (n >> i) & 1
            p = p.node[bit]
            
    def search(self, n):
        p = self.root
        res = 0
        for i in range(31, -1, -1):
            bit = (n >> i) & 1
            if (bit ^ 1) in p.node:
                p = p.node[bit ^ 1]
                res |= (1 << i)
            else:
                p = p.node[bit]
        return res


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        trie = Trie()
        for n in nums:
            res = max(res, trie.search(n))
            trie.insert(n)
        return res