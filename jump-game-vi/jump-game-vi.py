class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import collections
        ln = len(nums)
        bf = collections.deque([0])
        for i in range(1, ln):
            if bf and bf[0] + k < i:
                bf.popleft()
            cur = nums[bf[0]] + nums[i]
            while bf and cur > nums[bf[-1]]:
                bf.pop()
            nums[i] = cur
            bf.append(i)
        return nums[bf[-1]]