class RandomizedSet(object):

    def __init__(self):
        self.ls = [] 
        self.pos = {}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            self.pos[val] = len(self.pos)
            self.ls.append(val)
            return True
        return False
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            ival = self.pos[val]
            
            ilast, last = len(self.ls) - 1, self.ls[-1]
            
            self.ls[ival] = last 
            self.pos[last] = ival 
            
            self.ls.pop()
            del self.pos[val]
            return True
        
        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        import random
        return random.choice(self.ls)