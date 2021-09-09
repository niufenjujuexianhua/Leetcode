class unionfind(object):
    def __init__(self, nums):
        self.p = list(range(len(nums)))
        self.sz = [1] * len(nums)
        self.mx = 1

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.sz[px] < self.sz[py]:
                self.p[px] = py
                self.sz[py] += self.sz[px]
                self.sz[px] = 0
                self.mx = max(self.mx, self.sz[py])
            else:
                self.p[py] = px
                self.sz[px] += self.sz[py]
                self.sz[py] = 0
                self.mx = max(self.mx, self.sz[px])


class Solution(object):
    def largestComponentSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_primes(n):
            for prm in range(2, int(n ** 0.5) + 1):
                if n % prm == 0:
                    return get_primes(n // prm) | set([prm])
            return set([n])

        uf = unionfind(nums)
        prm_dt = collections.defaultdict(set)

        for i, n in enumerate(nums):
            primes = get_primes(n)
            for prm in primes:
                prm_dt[prm].add(i)

        for prm in prm_dt:
            idx = prm_dt[prm].pop()
            for i in prm_dt[prm]:
                uf.union(idx, i)

        return uf.mx
