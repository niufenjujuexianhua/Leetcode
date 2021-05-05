class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        if not 0 in arr:
            return False

        n = len(arr)
        return self.dfs(arr, start, n, {})

    def dfs(self, arr, i, n, memo):
        # print(i)
        if i < 0 or i >= n:
            return False

        if arr[i] == 0:
            return True

        if i in memo:
            return memo[i]

        memo[i] = False
        if self.dfs(arr, i + arr[i], n, memo):
            memo[i] = True
            return memo[i]

        if self.dfs(arr, i - arr[i], n, memo):
            memo[i] = True
            return memo[i]

        return memo[i]
        