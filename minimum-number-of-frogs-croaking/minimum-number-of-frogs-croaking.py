class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        d = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        ans = 0
        for e in croakOfFrogs:
            d[e] += 1

            if not (d['c'] >= d['r'] >= d['o'] >= d['a'] >= d['k']):
                return -1

            ans = max(ans, d['c'] - d['k'])

        if not d['c'] == d['r'] == d['o'] == d['a'] == d['k']:
            return -1
        return ans 