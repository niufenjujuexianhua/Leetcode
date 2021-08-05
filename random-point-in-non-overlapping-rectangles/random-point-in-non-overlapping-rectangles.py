class Solution(object):
    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.w = []
        for a, b, x, y in rects:
            if not self.w:
                self.w.append((x - a + 1) * (y - b + 1))
            else:
                self.w.append((x - a + 1) * (y - b + 1) + self.w[-1])
        

    def pick(self):
        """
        :rtype: List[int]
        """
        import random
        rand = random.randint(1, self.w[-1])
        s, e = 0, len(self.w) - 1
        while s + 1 < e:
            m = s + (e - s) // 2
            # if self.w[m] == rand:

            if self.w[m] > rand:
                e = m
            else:
                s = m
        if self.w[s] >= rand:
            i = s
        else:
            i = e

        return [random.randint(self.rects[i][0], self.rects[i][2]),
                random.randint(self.rects[i][1], self.rects[i][3])]