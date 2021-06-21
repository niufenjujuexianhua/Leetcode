class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st = []
        for i, n in enumerate(nums):
            if not st or nums[st[-1]] > n:
                st.append(i)

        res = 0
        for j in reversed(range(len(nums))):
            while st and nums[j] >= nums[st[-1]]:
                res = max(res, j - st.pop())
        return res 