class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        n = 0
        op = '+'
        for i, ch in enumerate(s):
            # if ch == ' ':
            #     continue

            if ch.isdigit():
                n = n * 10 + int(ch)
            if i == len(s) - 1 or ch in '+-*/':
                if op == '+':
                    st.append(n)
                elif op == '-':
                    st.append(-n)
                elif op == '*':
                    st.append(st.pop() * n)
                else:
                    st.append(int(st.pop() / float(n)))
                op = ch
                n = 0
        return sum(st)