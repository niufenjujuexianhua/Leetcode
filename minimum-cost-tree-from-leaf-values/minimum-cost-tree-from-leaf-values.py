class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        st, res = [float('inf')], 0
        for a in arr:
            while st and st[-1] <= a:
                drop = st.pop()
                res += drop * min(st[-1], a)
            st.append(a)

        while len(st) > 2:
            res +=  st.pop() * st[-1]

        return res 