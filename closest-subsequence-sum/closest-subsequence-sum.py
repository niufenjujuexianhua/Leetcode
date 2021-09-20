class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        sz = len(nums)
        # if sz == 1:
        #     return abs(goal - nums[0])

        # ltsums, rtsums = self.subsetSum(nums[:sz // 2]), self.subsetSum(nums[sz // 2:])
        ltsums, rtsums = set(), set()
        self.subsetSum(0,0,nums[:len(nums)//2],ltsums), self.subsetSum(0,0,nums[len(nums)//2:],rtsums)
        ltsums = sorted(list(ltsums))

        res = float('inf')
        for s in rtsums:
            target = goal - s
            res = min(res, self.bs(ltsums, target))
            if res == 0:
                break
        return res

    def bs(self, nums, target):
        s, e = 0, len(nums) - 1
        while s + 1 < e:
            m = s + (e - s) // 2
            if nums[m] == target:
                return 0
            elif nums[m] > target:
                e = m
            else:
                s = m

        return min(abs(nums[s] - target), abs(nums[e] - target))

    def subsetSum(self, i, cur, arr, sums):
        if i == len(arr):
            sums.add(cur)
            return
        self.subsetSum(i + 1, cur, arr, sums)
        self.subsetSum(i + 1, cur + arr[i], arr, sums)