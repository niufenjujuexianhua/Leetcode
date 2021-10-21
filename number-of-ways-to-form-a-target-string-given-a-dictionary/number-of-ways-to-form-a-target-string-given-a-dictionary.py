class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m = len(words[0])
        rec = [defaultdict(int) for _ in range(m)]
        for i in range(len(words)):
            for j in range(m):
                rec[j][words[i][j]] += 1
                
        @lru_cache(None)
        def ways(ind, t):
            if t >= len(target):
                return 1
            if (ind >= m): return 0
            ans = 0
            ans += ways(ind + 1, t + 1) * rec[ind][target[t]]
            ans += ways(ind + 1, t)
            return ans
        mod = int(1e9+7)
        return ways(0, 0) % mod