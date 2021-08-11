class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dt = {'(' : 0,
              '{' : 0,
              '[' : 0}
        map = {')' : '(',
               ']' : '[',
               '}' : '{'}
        st = []
        for ch in s:
            if st and ch in map and st[-1] == map[ch]:
                    st.pop()
            else:
                st.append(ch)

        return not st