class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        0 1 2 3 4 5
            i     j
        """
        pref = [0]
        for h in hours:
            pref.append(pref[-1] + (1 if h > 8 else -1))

        st = []
        for i in range(len(pref)):
            if not st or pref[st[-1]] > pref[i]:
                st.append(i)

        res = 0
        for j in reversed(range(len(pref))):
            while st and pref[st[-1]] < pref[j]:
                res = max(res, j - st[-1])
                st.pop()
        return res