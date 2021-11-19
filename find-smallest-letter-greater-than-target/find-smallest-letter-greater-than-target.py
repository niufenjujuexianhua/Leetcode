class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        s, e = 0, len(letters) - 1
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        # if target > letters[-1]:
        #     return letters[0]
        
        while s <= e:
            m = s + (e - s) // 2
            if letters[m] <= target:
                s = m + 1
            else:
                e = m - 1
        # print(s)
        # if letters[s] > target:
        return letters[s]