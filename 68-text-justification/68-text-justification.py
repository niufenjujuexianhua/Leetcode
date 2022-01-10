class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, i = [], 0

        while i < len(words):
            j = i
            curlen = 0
            while j < len(words) and curlen + len(words[j]) <= maxWidth:
                curlen += len(words[j]) + 1
                j += 1

            numwords = j - i
            if numwords == 1 or j == len(words):
                self.leftalign(res, words, i, j, maxWidth)
            else:
                self.midalign(res, words, i, j, maxWidth, curlen)

            i = j

        return res

    def leftalign(self, res, words, i, j, maxWidth):
        row = ''
        for k in range(i, j):
            row += words[k] + ' '
        row = row[:-1]
        row += ' ' * (maxWidth - len(row))
        res.append(row)
        return

    def midalign(self, res, words, i, j, maxWidth, curlen):
        spaceblock = j - i - 1
        spaces = maxWidth - curlen + (j - i)
        sz, remaining = divmod(spaces, spaceblock)

        row = ''
        for k in range(i, j):
            row += words[k] + ' ' * sz
            if remaining > 0:
                row += ' '
                remaining -= 1
        res.append(row[:maxWidth])
        return