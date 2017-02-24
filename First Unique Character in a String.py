class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        d = collections.Counter(s)

        for i, v in enumerate(s):
            if d[v] == 1:
                return i
        return -1

class Solution2(object):
    def firstUniqChar(self, s):

        map = {}
        for i in s:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1

        for i, v in enumerate(s):
            if map[v] == 1:
                return i

        return -1





if __name__ == '__main__':
    result = Solution().firstUniqChar("loveleetcode")
    print(result)