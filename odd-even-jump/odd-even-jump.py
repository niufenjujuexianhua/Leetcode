class Solution(object):
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        nexthigher, nextlower = [0] * n, [0] * n

        st = []
        for a, i in sorted([a, i] for i, a in enumerate(arr)):
            while st and st[-1] < i:
                nexthigher[st.pop()] = i
            st.append(i)

        st = []
        for a, i in sorted([-a, i] for i, a in enumerate(arr)):
            while st and st[-1] < i:
                nextlower[st.pop()] = i
            st.append(i)

        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1
        for i in reversed(range(n - 1)):
            higher[i] = lower[nexthigher[i]]
            lower[i] = higher[nextlower[i]]
        return sum(higher)