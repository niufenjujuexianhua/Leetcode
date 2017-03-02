class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        head, tail = -1, k
        if len(nums) <= k:
            return len(list(set(nums))) != len(nums)

        for i in range(len(nums) - k):
            head += 1
            tail += 1
            if len(list(set(nums[head:tail]))) != len(nums[head:tail]):
                return True
        return False

class Solution2(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dt = {}

        for i in range(len(nums)):
            if nums[i] in dt:
                if i - dt[nums[i]] <= k:
                    return True
                dt[nums[i]] = i
            else:
                dt[nums[i]] = i
        return False

class Solution3(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(set(nums)) == len(nums):
            return False

        for n in nums:
            p = [i for i, v in enumerate(nums) if v == n]
            q = [b-a for a, b in zip(p[:-1], p[1:])]
            if len(q) > 0:
                if min(q) <= k:
                    return True
        return False

if __name__ == '__main__':
    result = Solution3().containsNearbyDuplicate([-1,-1],1)
    print(result)