class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        import collections
        maxd = collections.deque()
        mind = collections.deque()

        i = res = 0
        for j in range(len(nums)):
            while maxd and nums[j] > maxd[-1]:
                maxd.pop()
            while mind and nums[j] < mind[-1]:
                mind.pop()

            maxd.append(nums[j])
            mind.append(nums[j])

            while maxd[0] - mind[0] > limit:
                if maxd[0] == nums[i]:
                    maxd.popleft()
                if mind[0] == nums[i]:
                    mind.popleft()
                i += 1
            res = max(res, j - i + 1)
        return res 