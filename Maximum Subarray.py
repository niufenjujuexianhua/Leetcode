class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        largest = 0
        substr = ''
        for i in range(len(nums)):
            sum += nums[i]
            for k in range(i + 1, len(nums)-1):
                sum += nums[k]
                if sum > sum + nums[k+1]:
                    largest = sum
                    substr = nums[i:k+1]
                    sum = 0
                    break


        return substr

class Solution1(object):
    def maxSubArray(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 0
        result = A[0]
        for i in A:
            current += i
            result = max(current, result)
            current = max(0, current)
        return result

class Solution2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
                nums[i] = max(nums[i - 1] + nums[i], nums[i])
        return max(nums)

class Solution3(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        T = nums[0]
        maxsub = T
        for i in nums[1:]:
            T += i
            if i > T:
                T = i
            if T > maxsub:
                maxsub = T
        return maxsub



class Solution4(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)





if __name__ == '__main__':
    result = Solution3().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(result)