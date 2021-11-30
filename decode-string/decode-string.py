class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        "3[a2[c]]"
                i
         n=0
         st=[3, [, 'acc']
        """
        st = ['']
        n = 0
        for i in range(len(s)):
            ch = s[i]
            if ch == ']':
                letter = st.pop()
                st.pop()
                n = st.pop()
                st[-1] += letter * n
                n = 0
            elif ch == '[':
                st.append(n)
                st.append(ch)
                st.append('')
                n = 0
            elif ch.isdigit():
                n = n * 10 + int(ch)
            else: # letter
                st[-1] += ch
        return ''.join(st)