class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        excluded = []
        for n in nums:
            if (n in excluded):
                return True
            excluded.append(n)
        return False