class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st =[]

        for t in tokens:
            if t not in '+-*/':
                st.append(int(t))
            else:
                second = st.pop()
                first = st.pop()

                if t == '+': val = first + second
                if t == '-': val = first - second
                if t == '*': val = first * second
                if t == '/': val = int(float(first) / float(second))

                st.append(val)
        return st[0]