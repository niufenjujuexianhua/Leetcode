class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        while x > 0 or y > 0:
            if x % 2 != y % 2:
                count += 1
            x = x // 2
            y = y // 2

        return count


class Solution2(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count("1")



# class Solution3(object):
#     # @param n, an integer
#     # @return an integer
#     def hammingDistance(self, n):
#         cnt = 0
#         while n:
#             if n&1: cnt+=1
#             n>>=1
#         return cnt

if __name__ == '__main__':
    result = Solution3().hammingDistance(7,8)
    print(result)