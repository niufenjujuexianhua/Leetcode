class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ls = []
        self.pos = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            self.ls.append(val)
            self.pos[val] = len(self.ls) - 1
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            i = self.pos[val]
            self.ls[i], self.ls[len(self.ls) - 1] = self.ls[len(self.ls) - 1], self.ls[i]
            self.pos[self.ls[i]] = i
            del self.pos[self.ls[-1]]
            self.ls.pop()
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        return random.choice(self.ls)