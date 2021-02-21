class Solution:
    """
    @param target: a target string
    @param dictionary: a set of strings in a dictionary
    @return: an abbreviation of the target string with the smallest possible length
    """

    def minAbbreviation(self, target, dictionary):
        # Write your code here
        import heapq
        dictionary = [cand for cand in dictionary if len(cand) == len(target)]
        q = []
        self.bt(target, 0, 0, '', q)

        while q:
            noconflict = True
            _, abbr = heapq.heappop(q)
            for word in dictionary:
                if self.validWordAbbreviation(word, abbr):
                    noconflict = False
                    break
            if noconflict:
                return abbr

    def bt(self, word, i, cnt, path, res):
        import heapq
        if i == len(word):
            path += ['', str(cnt)][cnt != 0]
            heapq.heappush(res, (len(path), path))
            return

        self.bt(word, i + 1, cnt + 1, path, res)
        self.bt(word, i + 1, 0, path + ['', str(cnt)][cnt != 0] + word[i], res)

    def validWordAbbreviation(self, word, abbr):
        # write your code here
        m, n = len(word), len(abbr)
        i, j = 0, 0

        while i < m and j < n:
            if abbr[j].isdigit():
                if abbr[j] == '0': return False

                k = j
                while k < n and abbr[k].isdigit(): k += 1
                num = int(abbr[j: k])
                j = k
                i += num
            else:
                if word[i] != abbr[j]: return False
                i += 1
                j += 1

        return i == m and j == n


print(Solution().minAbbreviation("apple",["plain","amber","blade"]))