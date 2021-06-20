class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        st =[]
        for i, n in enumerate(nums):
            while st and st[-1] > n and len(st) - 1 + len(nums) - i >= k:
                st.pop()
            if len(st) < k:
                st.append(n)
        return st