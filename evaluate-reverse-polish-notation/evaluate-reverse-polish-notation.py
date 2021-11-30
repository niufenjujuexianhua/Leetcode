class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st = []

        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                st.append(int(t))
            else:
                sec = st.pop()
                fir = st.pop()

                if t == '+':
                    st.append(fir + sec)
                elif t == '-':
                    st.append(fir - sec)
                elif t == '*':
                    st.append(fir * sec)
                else:
                    st.append(int(float(fir) / sec))
        return st[-1]