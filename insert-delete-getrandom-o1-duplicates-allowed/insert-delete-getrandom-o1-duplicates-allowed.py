class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.ls = []
        self.pos = collections.defaultdict(set)
        self.cnt = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.pos[val].add(len(self.ls))
        self.ls.append(val)

        return len(self.pos[val]) == 1

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.pos[val]:
            return False

        i = self.pos[val].pop()
        self.ls[i] = self.ls[-1]
        self.pos[self.ls[-1]].add(i)
        self.pos[self.ls[-1]].discard(len(self.ls) - 1)
        self.ls.pop()
        return True 

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        return random.choice(self.ls)