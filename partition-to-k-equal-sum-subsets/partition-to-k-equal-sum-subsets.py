class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums.sort(reverse = True)
        total = sum(nums)
        if total % k != 0:
            return False
        total //= k
        if nums[0] > total:
            return False 
        return self.dfs(nums, 0, k, 0, total)

    def dfs(self, nums, used, k, ss, target):
        if ss == target:
            return self.dfs(nums, used, k - 1, 0, target)
        if used == ((1 << len(nums)) - 1):
            return k == 0

        for i in range(len(nums)):
            if used & (1 << i) or ss + nums[i] > target:
                continue
            if self.dfs(nums, used | (1 << i), k, ss + nums[i], target):
                return True
        return False