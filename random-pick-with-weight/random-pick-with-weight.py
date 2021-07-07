class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        prob = 1.0 / sum(w)
        self.w = [0] * len(w)
        for i, weight in enumerate(w):
            if i == 0:
                self.w[i] = prob * weight
            else:
                self.w[i] = prob * weight + self.w[i - 1]
        

    def pickIndex(self):
        """
        :rtype: int
        """
        p = random.random()
        s, e = 0, len(self.w) - 1
        while s + 1 < e:
            m = s + (e - s) // 2
            if self.w[m] > p:
                e = m
            else:
                s = m
        if self.w[s] >= p:
            return s
        return e 