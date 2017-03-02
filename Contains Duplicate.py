class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return bool(len(nums) - len(set(nums)))

        return len(nums) != len(set(nums))

class Solution2(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) in (0, 1):
            return False

        dt = {}
        for i in nums:
            if i in dt:
                return True
            else:
                dt[i] = 1
        return False


class Solution3(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import collections

        return bool(len(nums) - len(collections.Counter(nums)))
if __name__ == '__main__':
    result = Solution3().containsDuplicate([0])
    print(result)