class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        return s

class Solution1(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for i in s:
            res.insert(0,i)
        return ''.join(res)

class Solution2(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in range(len(s)-1, -1, -1):
            res += s[i]
        return res


class Solution3(object):
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])

class Solution4(object):
    def reverseString(self, s):
        r = list(s)
        i, j  = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1

        return "".join(r)

class Solution5(object):
    def reverseString(self, s):
        n = len(s)
        s = list(s)

        for i in range(n / 2):
            s[i], s[~i] = s[~i], s[i]

        return "".join(s)

if __name__ == '__main__':
    result = Solution2().reverseString('hello')
    print(result)