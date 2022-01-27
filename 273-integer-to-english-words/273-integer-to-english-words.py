class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        self.LESS20 = ['', 'One', "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.LESS100 = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        res = self.dfs(num)
        return res.strip()

    def dfs(self, n):
        res = '' 
        if n < 20:
            res = self.LESS20[n]
        elif n < 100: #98
            res = self.LESS100[n // 10] + ' ' + self.dfs(n % 10)
        elif n < 1000: #897
            res = self.LESS20[n // 100] + ' Hundred ' + self.dfs(n % 100)
        elif n < 1000000: #897 655
            res = self.dfs(n // 1000) + ' Thousand ' + self.dfs(n % 1000)
        elif n < 1000000000: #897 655 321
            res = self.dfs(n // 1000000) + ' Million ' + self.dfs(n % 1000000)
        elif n < 1000000000000:
            res = self.dfs(n // 1000000000) + ' Billion ' + self.dfs(n % 1000000000)
        return res.strip()