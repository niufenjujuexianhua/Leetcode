class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        maxn = 0
        for idx, val in enumerate(nums):
            if val == 1:
                cnt += 1
            else:
                maxn = max(maxn, cnt)
                cnt = 0
        return max(maxn, cnt)


class Solution1(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 not in nums:
            return len(nums)

        res = 0
        s = ''.join(str(i) for i in nums)
        l = s.split('0')
        for i in l:
            if len(i) > res:
                res = len(i)
        return res



if __name__ == '__main__':
    result = Solution1().findMaxConsecutiveOnes([1,1,0,1])
    print(result)