class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        l = 0
        r = 1
        for r in range(len(prices)):
            if (prices[r]<prices[l]):
                l = r
            else:
                maxPrice=max(maxPrice, prices[r]-prices[l])
        return maxPrice