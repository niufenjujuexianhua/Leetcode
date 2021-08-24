class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0:
            return a
        if a == 0:
            return b

        mask = 0xffffffff
        while b & mask > 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return (a & mask) if b > 0 else a
print(Solution().getSum(-1, 1))
# leetcode submit region end(Prohibit modification and deletion)
