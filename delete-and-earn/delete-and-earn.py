class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        3 1 1 3 1
        1 2 5 6
        3 3 7 18 13

        p[i] = max(p[i - 1], p[i - 2] + cur * freq)
        """
        import collections
        freq = collections.Counter(nums)
        take, notake = 0, 0
        prev = None 

        for n in sorted(freq):
            f = freq[n]
            tmptake, tmpnotake = take, notake
            if n - 1 != prev:
                take = n * f + max(tmptake, tmpnotake)
            else:
                take = n * f + tmpnotake

            notake = max(tmptake, tmpnotake)
            prev = n 

        return max(take, notake)