class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        n = len(words)
        i = 0
        res = []
        while i < n:
            j = i + 1
            linelen = len(words[i])

            while j < n and linelen + len(words[j]) + j - i <= maxWidth:
                linelen += len(words[j])
                j += 1

            if j == n or j - i == 1:
                self.leftjustify(res, words, i, j, maxWidth, linelen)
            else:
                self.midjustify(res, words, i, j, maxWidth, linelen)

            i = j
        return res

    def leftjustify(self, res, words, i, j, maxWidth, linelen):
        s = ''
        # diff = maxWidth - linelen - (j - i)
        for k in range(i, j):
            s += words[k]
            s += ' '
        if len(s) < maxWidth:
            s += ' ' * (maxWidth - len(s))
        if len(s) > maxWidth:
            s = s[:maxWidth]
        res.append(s)

    def midjustify(self, res, words, i, j, maxWidth, linelen):
        s = ''
        spaceblocks = j - i - 1
        numspaces = (maxWidth - linelen) // spaceblocks
        remaining = (maxWidth - linelen) % spaceblocks
        for k in range(i, j):
            s += words[k]
            s += ' ' * numspaces
            if remaining > 0:
                s += ' '
                remaining -= 1
        s = s[:-numspaces]
        res.append(s)