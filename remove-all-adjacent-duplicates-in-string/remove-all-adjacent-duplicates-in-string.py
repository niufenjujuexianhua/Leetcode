class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []
        for ch in s:
            if st and ch == st[-1]:
                st.pop()
            else:
                st.append(ch)
        return ''.join(st)