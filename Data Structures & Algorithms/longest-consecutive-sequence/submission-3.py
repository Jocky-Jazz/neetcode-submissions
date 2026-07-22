class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cons={}
        nums.sort()
        for n in nums:
            if ((n-1) in cons):
                cons[n] = cons[n-1]+1
            else:
                cons[n] = 1
        return max(cons.values() or [0,])
