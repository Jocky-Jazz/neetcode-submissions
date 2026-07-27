class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices = list(enumerate(prices))
        l, r = (0, 0), (0, 0)
        maxPrice = 0
        while(r[0] < len(prices)):
            r = max(prices[r[0]:], key=lambda x:x[1])
            if (r[0] > 0):
                l = min(prices[l[0]:r[0]], key=lambda x:x[1])
                maxPrice=max(maxPrice, r[1]-l[1])
            #print(prices[r][1], l, maxPrice)
            r = (r[0]+1, r[1])
        return maxPrice