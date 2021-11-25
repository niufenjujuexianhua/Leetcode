class Node():
    def __init__(self, key, val):
        self.key = key
        self.val = val

class MyHashMap(object):

    def __init__(self):
        self.sz = 10 ** 5
        self.bucket = [[] for _ in range(self.sz)]

    def find(self, key, hs):
        # hs = key % self.sz
        for i, node in enumerate(self.bucket[hs]):
            if node.key == key:
                return i
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hs = key % self.sz
        i = self.find(key, hs)
        if i == -1:
            self.bucket[hs].append(Node(key, value))
        else:
            self.bucket[hs][i].val = value
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        hs = key % self.sz
        i = self.find(key, hs)
        if i != -1:
            return self.bucket[hs][i].val
        return -1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hs = key % self.sz
        i = self.find(key, hs)
        if i != -1:
            self.bucket[hs].pop(i)