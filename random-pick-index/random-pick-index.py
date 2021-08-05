class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dt = collections.defaultdict(list)
        for i, n in enumerate(nums):
            self.dt[n].append(i)
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.dt[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)