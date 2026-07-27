class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices = list(enumerate(prices))
        l, r = 0, 0
        r_ =0
        maxPrice = 0
        while(r_ < len(prices)):
            r = max(prices[r_:], key=lambda x:x[1])[0]
            if (r > 0):
                l = min(prices[:r], key=lambda x:x[1])[1]
                maxPrice=max(maxPrice, prices[r][1]-l)
            r_ = r+1
            #print(prices[r][1], l, maxPrice)
        return maxPrice