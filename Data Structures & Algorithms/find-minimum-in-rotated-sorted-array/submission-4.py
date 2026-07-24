class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        mid = 0
        while (l <= r):
            mid = l + ((r-l)>>1)
            if (nums[l]<=nums[mid] and nums[mid]<=nums[r]):
                return nums[l]
            elif (nums[l]>=nums[mid] and nums[mid]>=nums[r]):
                return nums[r]
            elif (nums[l]<nums[mid] and nums[mid]>nums[r]):
                l = mid
            elif (nums[l]>nums[mid] and nums[mid]<nums[r]):
                r = mid
        return nums[mid]