class UnionFind(object):
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.p[px] = py
                self.rank[py] += self.rank[px]
                self.rank[px] = 0
            else:
                self.p[py] = px
                self.rank[px] += self.rank[py]
                self.rank[py] = 0


class Solution(object):
    def gcdSort(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sz, mx = len(nums), max(nums)
        uf = UnionFind(mx + 1)
        seen = set(nums)

        primes = [1] * (mx + 1)
        primes[0] = primes[1] = 0
        for i in range(mx // 2 + 1):
            if primes[i] == 1:
                for j in range(i + i, mx + 1, i):
                    primes[j] = 0
                    if j in seen:
                        uf.union(j, i)


        # for n in nums:
        #     for i in range(2, mx + 1):
        #         if i > n: break
        #         if primes[i] == 1 and n % i == 0:
        #             uf.union(n, i)
        #             while n % i == 0:
        #                 n //= i


        for a, b in zip(nums, sorted(nums)):
            if uf.find(a) != uf.find(b):
                return False
        return True
