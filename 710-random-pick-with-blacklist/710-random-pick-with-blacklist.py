class Solution(object):

    def __init__(self, n, blacklist):
        """
        :type n: int
        :type blacklist: List[int]
        self.n = 4
        0 1 2 3 4 5
            x     x
        """
        blacklist = set(blacklist)
        self.n = n - len(blacklist)
        key = [x for x in blacklist if x < self.n]
        val = [x for x in range(self.n, n) if x not in blacklist]
        self.dt = dict(zip(key, val))
        

    def pick(self):
        """
        :rtype: int
        """
        i = random.randrange(0, self.n)
        return self.dt.get(i, i)