class Solution(object):
    def numSquarefulPerms(self, A):
        ret = []
        used = [0] * len(A)
        self.dfs(sorted(A), used, [], ret, len(A))
        return len(ret)

    def dfs(self, nums, used, path, ret, n):
        if len(path) == n:
            ret.append(path)
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue  # skip duplicates
            if path and not self.square(path[-1] + nums[i]):
                continue  # backtracking without going further
            used[i] = 1
            self.dfs(nums, used, path + [nums[i]], ret, n)
            used[i] = 0

    def square(self, num):
        from math import sqrt
        return pow(int(sqrt(num)), 2) == num