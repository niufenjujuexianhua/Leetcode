class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        cnt = collections.defaultdict(int)
        cnt[0] = 1 
        res = prefix = 0
        
        for n in nums:
            prefix += n
            res += cnt[prefix - goal]
            cnt[prefix] += 1
        return res