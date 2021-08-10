class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dt = collections.defaultdict(int)
        i = res = dup = 0

        for j, ch in enumerate(s):
            dt[ch] += 1
            if dt[ch] == 2:
                dup += 1

            while dup > 0 and i < len(s):
                dt[s[i]] -= 1
                if dt[s[i]] == 1:
                    dup -= 1
                i += 1

            res = max(res, j - i + 1)

        return res