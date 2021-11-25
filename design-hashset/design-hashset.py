class MyHashSet(object):

    def __init__(self):
        self.sz = 10 ** 6 + 1 
        self.bucket = [None] * self.sz 

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.bucket[key] is None:
            self.bucket[key] = key 
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.bucket[key] is not None:
            self.bucket[key] = None  
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.bucket[key] is not None