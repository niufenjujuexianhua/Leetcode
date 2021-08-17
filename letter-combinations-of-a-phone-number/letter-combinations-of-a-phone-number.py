class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return [] 
        dt = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
              '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = [] 
        self.dfs(digits, 0, dt, '', res)
        return res 
        
    def dfs(self, digits, i, dt, path, res):
        if len(path) == len(digits):
            res.append(path)
            return 

        for char in dt[digits[i]]:
            self.dfs(digits, i + 1, dt, path + char, res)