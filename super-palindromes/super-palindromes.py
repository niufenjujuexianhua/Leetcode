class Solution(object):
    def superpalindromesInRange(self, left, right):
        """
        :type left: str
        :type right: str
        :rtype: int
        1 18 0
        100000 00001
        """
        lt, rt = int(left), int(right)
        cnt = 0
        for i in range(1, 10 ** 5 + 1):
            si = str(i)
            esi = si + si[::-1]
            osi = si + si[:-1][::-1]

            esq = int(esi) ** 2
            osq = int(osi) ** 2
            if lt <= esq <= rt and self.pal(str(esq)):
                cnt += 1
            if lt <= osq <= rt and self.pal(str(osq)):
                cnt += 1
        return cnt

    def pal(self, n):
        return n == n[::-1]