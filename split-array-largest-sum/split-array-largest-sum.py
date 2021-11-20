class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        1,1   2
        """
        def valid(mid):
            cnt, sm = 1, 0
            for n in nums:
                if n > mid: return False
                if sm + n <= mid:
                    sm += n
                else:
                    sm = n
                    cnt += 1
            return cnt <= m

        
        s, e = max(nums), sum(nums) + 1
        while s < e:
            guess = s + (e - s) // 2
            if valid(guess):
                e = guess
            else:
                s = guess + 1 
        return s 