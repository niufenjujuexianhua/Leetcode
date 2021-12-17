class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        import collections
        dt = collections.defaultdict(set)

        for a, b in dislikes:
            dt[a].add(b)
            dt[b].add(a)

        colors = {}
        for i in range(1, n + 1):
            if i not in colors:
                if not self.twocolor(dt, i, 0, colors):
                    return False
        return True
    
    def twocolor(self, dt, i, c, colors):
        if i in colors:
            return colors[i] == c

        colors[i] = c
        for nxt in dt[i]:
            if not self.twocolor(dt, nxt, 1 - c, colors):
                return False
        return True