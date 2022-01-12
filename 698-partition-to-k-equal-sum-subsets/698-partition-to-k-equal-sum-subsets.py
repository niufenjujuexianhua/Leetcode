class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        target, remaining = divmod(total, k)
        if remaining:
            return False
        nums = sorted(nums, reverse = 1)
        if nums[0] > target:
            return False 
        return self.dfs(nums, 0, target, 0, k)

    def dfs(self, nums, used, target, cur, k):
        if cur == target:
            return self.dfs(nums, used, target, 0, k - 1)
        if used == (1 << len(nums)) - 1:
            return k == 0

        for i in range(len(nums)):
            if not used & (1 << i):
                if cur + nums[i] <= target:
                    # used[i] = 1
                    if self.dfs(nums, used | (1 << i), target, cur + nums[i], k):
                        return True
                    # used[i] = 0
        return False