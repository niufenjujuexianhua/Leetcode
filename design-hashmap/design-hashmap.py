class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sz = 100000
        self.bucket = [[] for _ in range(self.sz)]

    def find(self, key, hs):
        # hs = key % self.sz
        for i, (k, v) in enumerate(self.bucket[hs]):
            if k == key:
                return i, k, v
        return -1, -1, -1

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hs = key % self.sz
        i, k, v = self.find(key, hs)
        if i == -1:
            self.bucket[hs].append([key, value])
        else:
            self.bucket[hs][i][1] = value
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hs = key % self.sz
        i, k, v = self.find(key, hs)
        if i == -1:
            return -1
        return self.bucket[hs][i][1]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hs = key % self.sz
        i, k, v = self.find(key, hs)
        if i != -1:
            self.bucket[hs].remove([k, v])