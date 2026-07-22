class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []
        for i, n in enumerate(nums):
            if (i > 0 and n == nums[i-1]):
                continue
            j = i+1
            k = len(nums)-1
            while (j < k):
                if (n + nums[j] + nums[k] > 0):
                    k -= 1
                elif (n + nums[j] + nums[k] < 0):
                    j += 1
                else:
                    solutions.append([n, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while (j < k and nums[j] == nums[j - 1]):
                        j += 1
        return solutions
