class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss, st = list(s), []
        for i, ch in enumerate(ss):
            if ch == ')':
                if st: st.pop()
                else: ss[i] = ''
            elif ch == '(':
                st.append(i)

        for i in st:
            ss[i] = ''
        return ''.join(ss)