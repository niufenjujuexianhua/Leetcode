class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(map(int, list(s)))
        prefix = [0]
        for n in s:
            prefix.append(prefix[-1] + n)

        res = float('inf')
        for i in range(len(prefix)):
            oneslt = prefix[i] #ones in left
            zerosrt = len(s) - i - (prefix[-1] - prefix[i])
            res = min(res, oneslt + zerosrt)
        return res