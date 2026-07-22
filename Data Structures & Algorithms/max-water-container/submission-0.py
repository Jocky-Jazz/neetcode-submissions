class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        maxcap = 0
        while (i < j):
            maxcap = max(maxcap, (j-i)*min(heights[i],heights[j]))
            if (heights[i]<heights[j]):
                i += 1
            else:
                j -= 1
        return maxcap