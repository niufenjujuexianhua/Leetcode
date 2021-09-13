class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        cands = ['']
        res = 0

        for word in arr:
            for cand in cands:
                tmp = cand + word
                if len(tmp) == len(set(tmp)):
                    cands.append(tmp)
                    res = max(res, len(tmp))
        return res 