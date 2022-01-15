class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        dq = collections.deque()
        res = [] 
        for j, n in enumerate(nums):
            while dq and j - dq[0] + 1 > k:
                dq.popleft()
            
            while dq and nums[dq[-1]] < n:
                dq.pop()
            dq.append(j)
            
            if j >= k - 1:
                res.append(nums[dq[0]])
        return res 