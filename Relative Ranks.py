class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = [None] * len(nums)
        pair = dict([v, i] for i, v in enumerate(nums))
        nums = sorted(nums, reverse=True)

        for i, v in enumerate(nums):
            if i == 0:
                res[pair[v]] = 'Gold Medal'
            elif i == 1:
                res[pair[v]] = 'Silver Medal'
            elif i == 2:
                res[pair[v]] = 'Bronze Medal'
            else:
                res[pair[v]] = str(i + 1)

        return res

class Solution2(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sort = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums) + 1))
        return map(dict(zip(sort, rank)), nums)

if __name__ == '__main__':
    result = Solution2().findRelativeRanks([10,3,8,9,4])
    print(result)