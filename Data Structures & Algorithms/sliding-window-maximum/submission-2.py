class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxim = max(nums[:k])
        if (len(nums)<=k):
            return [maxim]
        i = 0
        res = [maxim]
        for i in range(1, len(nums)-k+1):
            if (nums[i-1] == maxim):
                maxim = max(nums[i:i+k])
            elif (nums[i+k-1] > maxim):
                maxim = nums[i+k-1]
            res.append(maxim)
        return res