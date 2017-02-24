class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            s, t = t, s
        s = sorted(s)
        t = sorted(t)

        for i in range(len(t)):
            if t[i] != s[i]:
                return s[i]
        return s[-1]


class Solution2(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        k = 0
        if len(s) < len(t):
            s, t = t, s
        for i in range(len(t)):
            k -= ord(t[i])
            k += ord(s[i])
        k += ord(s[-1])

        return chr(k)

class Solution3(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = -sum(ord(i) for i in s)
        t = sum(ord(i) for i in t)

        return chr(abs(s + t))

if __name__ == '__main__':
    result = Solution3().findTheDifference("abcd","abcde")
    print(result)