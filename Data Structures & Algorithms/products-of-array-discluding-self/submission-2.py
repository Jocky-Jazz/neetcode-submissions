class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list = [[]]*len(nums)
        for i, n in enumerate(nums):
            product_list[i] = nums[0:i]+nums[i+1:]
        product = [0]*len(nums)
        for i, n in enumerate(product_list):
            product[i] = math.prod(n)
        return product