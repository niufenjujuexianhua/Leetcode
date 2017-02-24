class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in findNums:
            index = nums.index(i)
            if index != len(nums) - 1:
                for k in nums[index+1:]:
                    if k > i:
                        res.append(k)
                        break
                    if k == nums[-1]:
                        res.append(-1)
            else:
                res.append(-1)
        return res


class Solution2(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        cache = {}
        st = []
        res = []

        for i in nums:
            while st and st[-1] < i:
                cache[st[-1]] = i
                st.pop()
            st.append(i)

        for k in findNums:
            if k in cache:
                res.append(cache[k])
            else:
                res.append(-1)
        return res

class Solution3(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res =[]
        for i in findNums:
            for k in nums[nums.index(i):]:
                if k > i:
                    res.append(k)
                    break
                if k == nums[-1]:
                    res.append(-1)
        return res

if __name__ == '__main__':
    result = Solution3().nextGreaterElement([4,1,2],[1,3,4,2])
    print(result)