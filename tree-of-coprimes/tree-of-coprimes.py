class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        from math import gcd
        res = [-1] * len(nums)
        path = [[] for _ in range(51)]
        g = collections.defaultdict(list)

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        self.dfs(g, 0, 0, nums, path, set(), res)
        return res

    def dfs(self, g, ni, d, nums, path, seen, res):
        if ni in seen:
            return
        seen.add(ni)
        dtmp = -1
        for x in range(1, 51):
            if gcd(x, nums[ni]) == 1 and path[x]:
                ansi, ansd = path[x][-1]
                if ansd > dtmp:
                    dtmp, res[ni] = ansd, ansi


        path[nums[ni]].append((ni, d))
        for neii in g[ni]:
            self.dfs(g, neii, d + 1, nums, path, seen, res)
        path[nums[ni]].pop()