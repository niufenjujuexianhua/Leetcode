class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        for i in range(1, len(w)):
            w[i] += w[i - 1]
        self.w = w

    def pickIndex(self):
        """
        :rtype: int
        """
        rand = random.randint(1, self.w[-1])
        s, e = 0, len(self.w) - 1
        while s + 1 < e:
            m = s + (e - s) // 2
            if self.w[m] > rand:
                e = m
            else:
                s = m
        if self.w[s] >= rand:
            return s
        return e 
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()