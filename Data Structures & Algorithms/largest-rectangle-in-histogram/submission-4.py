class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        #monotonically increasing stack
        for i, h in enumerate(heights):
            if (not stack or stack[-1][1]<h):
                stack.append((i, h))
            else:
                k = -1
                while(stack and stack[-1][1]>=h):
                    k = stack.pop()
                    maxarea = max(maxarea, k[1]*(i - k[0])) 
                stack.append((k[0], h))
        for i, h in stack:
            maxarea = max(maxarea, h*(len(heights)-i))
        return maxarea
