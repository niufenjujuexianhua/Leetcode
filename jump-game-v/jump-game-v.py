class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        m = {}
        return max([self.dfs(arr, j, m, d) for j in range(len(arr))])

    def dfs(self, arr, j, m, d):
        if j in m:
            return m[j]
        ans = 1
        for dir in [1, -1]:
            for dj in range(1, d + 1):
                nj = j + dir * dj
                if 0 <= nj < len(arr) and arr[nj] < arr[j]:
                    ans = max(ans, self.dfs(arr, nj, m, d) + 1)
                else:
                    break

        m[j] = ans
        return ans