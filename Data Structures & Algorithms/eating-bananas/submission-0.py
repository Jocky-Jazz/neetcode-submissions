class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        mid = 0
        while (l < r):
            mid = l + ((r-l)>>1)
            time = sum(math.ceil(p/mid) for p in piles)
            if (time > h):
                l = mid+1
            elif (time <= h):
                r = mid
        return l