class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sz = 100000
        self.bucket = [[] for _ in range(self.sz)]

    def find(self, key, hs):
        # hs = key % self.sz
        for i, v in enumerate(self.bucket[hs]):
            if v == key:
                return i, key
        return -1, key

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hs = key % self.sz
        i, v = self.find(key, hs)
        if i == -1:
            self.bucket[hs].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hs = key % self.sz
        i, v = self.find(key, hs)
        if i >= 0:
            self.bucket[hs].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hs = key % self.sz
        i, v = self.find(key, hs)
        if i >= 0:
            return True
        return False
        