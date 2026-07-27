class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices = list(enumerate(prices))
        l, r = 0, 0
        maxPrice = 0
        while(r < len(prices)):
            r = max(prices[r:], key=lambda x:x[1])[0]
            if (r > 0):
                l = min(prices[l:r], key=lambda x:x[1])[0]
                maxPrice=max(maxPrice, prices[r][1]-prices[l][1])
            #print(prices[r][1], l, maxPrice)
            r += 1
        return maxPrice