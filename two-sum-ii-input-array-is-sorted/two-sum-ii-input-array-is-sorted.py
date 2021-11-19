class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            
            s, e = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while s <= e:
                m = s + (e - s) // 2 
                if numbers[m] == tmp:
                    return [i + 1, m + 1]
                elif numbers[m] < tmp:
                    s = m + 1 
                else:
                    e = m - 1 
        return [-1, -1]