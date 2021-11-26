class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dt = collections.Counter(s)
        for i, c in enumerate(s):
            if dt[c] == 1:
                return i 
        return -1 