class Solution:
    """
    @param word: the given word
    @return: the generalized abbreviations of a word
    """
    def generateAbbreviations(self, word):
        # Write your code here
        res = []
        self.bt(word, 0, 0, '', res)
        return res

    def bt(self, word, i, cnt, path, res):
        if i == len(word):
            res.append(path + ['', str(cnt)][cnt != 0])
            return

        self.bt(word, i + 1, cnt + 1, path, res)
        self.bt(word, i + 1, 0, path + ['', str(cnt)][cnt != 0] + word[i], res)