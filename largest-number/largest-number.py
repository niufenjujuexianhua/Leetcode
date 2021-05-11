class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))
        res = ''.join(self.dfs(nums, 0, len(nums) - 1))
        if set(res) == set('0'):
            return '0'
        return res


    def dfs(self, nums, s, e):
        if s > e:
            return
        if s == e:
            return [nums[s]]

        m = s + (e - s) // 2
        lt = self.dfs(nums, s, m)
        rt = self.dfs(nums, m + 1, e)

        nn = []
        i, j = 0, 0
        while i < len(lt) and j < len(rt):
            if self.comp(lt[i], rt[j]):
                nn.append(lt[i])
                i += 1
            else:
                nn.append(rt[j])
                j += 1
        while i < len(lt):
            nn.append(lt[i])
            i += 1
        while j < len(rt):
            nn.append(rt[j])
            j += 1
        return nn

    def comp(self, i, j):
        return i + j > j + i