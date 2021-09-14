class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        ids, i = {}, 0
        for fc in favoriteCompanies:
            for c in fc:
                if c not in ids:
                    ids[c] = i
                    i += 1

        bits = []
        for fc in favoriteCompanies:
            bit = 0
            for c in fc:
                bit |= 1 << ids[c]
            bits.append(bit)

        res = []
        for i in range(len(bits)):
            flag = True
            for j in range(len(bits)):
                if i != j and bits[i] & bits[j] == bits[i]:
                    flag = False
                    break
            if flag:
                res.append(i)
        return res