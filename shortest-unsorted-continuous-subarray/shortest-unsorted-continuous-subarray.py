class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st = []
        for i in range(len(nums)):
            while st and st[-1] > nums[i]:
                st.pop()
            st.append(nums[i])
        if len(st) == len(nums): return 0

        for i in range(len(st)):
            if st[i] != nums[i]:
                lt = i
                break

        st = []
        for i in reversed(range(len(nums))):
            while st and st[-1] < nums[i]:
                st.pop()
            st.append(nums[i])

        for i in range(len(st)):
            if st[i] != nums[len(nums) - i - 1]:
                rt = len(nums) - i - 1
                break

        return rt - lt + 1