class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, maxl, maxr = 0, len(height)-1, 0, 0
        volume = 0
        while (l < r):
            if (height[l] < height[r]):
                maxl = max(maxl, height[l])
                volume += maxl - height[l]
                l += 1
            else:
                maxr = max(maxr, height[r])
                volume += maxr - height[r]
                r -= 1
        return volume