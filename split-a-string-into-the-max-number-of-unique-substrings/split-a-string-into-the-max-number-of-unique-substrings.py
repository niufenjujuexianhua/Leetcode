class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = [0]
        self.dfs(s, set(), res)
        return res[0]

    def dfs(self, s, seen, res):
        if not s:
            res[0] = max(res[0], len(seen))
            return
        if len(seen) + len(s) <= res[0]:
            return

        for i in range(len(s)):
            subs = s[: i + 1]
            if subs in seen:
                continue
            self.dfs(s[i + 1:], seen | set([subs]), res)