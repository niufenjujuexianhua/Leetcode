class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import collections
        dq = collections.deque([[0, nums[0]]])
        for i, n in enumerate(nums[1:], 1):
            if dq and dq[0][0] + k < i:
                dq.popleft()
            cur = dq[0][1] + n
            while dq and cur >= dq[-1][1]:
                dq.pop()
            dq.append([i, cur])
        return dq[-1][1]
# print(Solution().maxResult([1,2,3], 4))
