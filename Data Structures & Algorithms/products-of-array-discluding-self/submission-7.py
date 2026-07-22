class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [0]*len(nums)
        for i, n in enumerate(nums):
            product[i] = math.prod(nums[0:i]+nums[i+1:])
        return product