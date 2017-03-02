class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        import collections
        if len(s) != len(t):
            return False

        ds = collections.Counter(s)
        dt = collections.Counter(t)

        for k in ds:
            if k not in dt:
                return False
            elif ds[k] != dt[k]:
                return False

        return True



class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ds, dt = {}, {}

        for i in s:
            ds[i] = ds.get(i, 0) + 1
        for i in t:
            dt[i] = dt.get(i, 0) + 1
        return ds == dt

class Solution3(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


class Solution4(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            for i in set(s):
                if s.count(i) != t.count(i):
                    return False
            return True
        else:
            return False

if __name__ == '__main__':
    result = Solution4().isAnagram("aacc", "ccac")
    print(result)