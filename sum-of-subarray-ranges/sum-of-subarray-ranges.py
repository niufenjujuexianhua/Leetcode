class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        st = []
        for i in range(len(nums) + 1):
            while st and (i == len(nums) or nums[st[-1]] < nums[i]):
                mid = st.pop()
                ii = st[-1] if st else -1
                res += nums[mid] * (i - mid) * (mid - ii)
            st.append(i)


        st = []
        for i in range(len(nums) + 1):
            while st and (i == len(nums) or nums[st[-1]] > nums[i]):
                mid = st.pop()
                ii = st[-1] if st else -1
                res -= nums[mid] * (i - mid) * (mid - ii)
            st.append(i)

        return res 