class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, v in enumerate(numbers):
            for i2, v2 in enumerate(numbers[i+1:]):
                if (target - v) == v2:
                    return [i+1, i2+i+2]

class Solution2(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1

        for i in range(len(numbers)):
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1


class Solution3(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}

        for i, v in enumerate(numbers):
            if target-v in dict:
                return [dict[target-v]+1, i+1]
            dict[v] = i


if __name__ == '__main__':
    result = Solution3().twoSum([2, 7, 11, 15], 22)
    print(result)