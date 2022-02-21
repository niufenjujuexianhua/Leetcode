class Solution:
    """
    @param s: the expression string
    @return: the answer
    """

    def __init__(self):
        self.i = 0

    def calculate(self, s):
        # Write your code here
        st = []
        num = 0
        op = '+'

        while self.i < len(s):
            c = s[self.i]
            self.i += 1

            if c.isdigit():
                num = num * 10 + int(c)
            if c == '(':
                num = self.calculate(s)
            if self.i >= len(s) or c in '+-*/)':
                if op == '+':
                    st.append(num)
                elif op == '-':
                    st.append(-num)
                # elif op == '*':
                #     st.append(st.pop() * num)
                # elif op == '/':
                #     st.append(int(st.pop() * 1.0 / num))
                op = c
                num = 0
            if c == ')':
                break
        return sum(st)
        