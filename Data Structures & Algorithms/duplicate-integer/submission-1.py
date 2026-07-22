class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newlist = list(set(nums))
        return not (len(nums) == len(newlist) )