class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                sum += prices[i+1] - prices[i]
        return sum



class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1))

if __name__ == '__main__':
    result = Solution().maxProfit([1,3,6,2])
    print(result)