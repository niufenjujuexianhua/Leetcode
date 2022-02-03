class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        curn = 0
        prevop = '+'
        st = []

        for i, ch in enumerate(s):
            # if ch == ' ':
            #     continue
            if ch.isdigit():
                curn = curn * 10 + int(ch)
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                if prevop == '-':
                    st.append(curn * -1)
                elif prevop == '+':
                    st.append(curn)
                elif prevop == '*':
                    pren = st.pop()
                    st.append(pren * curn)
                elif prevop == '/':
                    pren = st.pop()
                    st.append(int(pren / float(curn)))
                curn = 0
                prevop = ch
        return sum(st)