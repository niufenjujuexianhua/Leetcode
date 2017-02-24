class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x

        while l <= r:
            mid = (l + r) // 2

            if mid ** 2 > x:
                r = mid - 1
            else:
                if (mid + 1) ** 2 > x:
                    return mid
                else:
                    l = mid + 1



if __name__ == '__main__':
    result = Solution().mySqrt(0)
    print(result)