class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = 0
        res = 0

        for e in s:
            if i > len(g)-1:
                break
            if e >= g[i]:
                res += 1
                i += 1

        return res



class Solution2(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = 0
        res = 0

        while i < min(len(g), len(s)):
            if s[i] >= g[i]:
                res += 1
                s.pop(i)
                g.pop(i)
            else:
                s.pop(i)
        return res


class Solution3(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i, j = 0, 0
        res = 0

        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                i += 1
                j += 1
                res += 1
            else:
                i += 1
        return res



if __name__ == '__main__':
    result = Solution3().findContentChildren([1,2,2], [1,1])
    print(result)