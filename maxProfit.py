class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        smallestNumber = prices[0]
        for i in range(len(prices)):
            if prices[i] < smallestNumber:
                smallestNumber = prices[i]
            else:
                newMax = prices[i] - smallestNumber
                if newMax > maxProfit:
                    maxProfit = newMax
        return maxProfit