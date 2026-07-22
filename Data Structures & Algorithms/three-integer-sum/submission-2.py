class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []
        for i, n in enumerate(nums):
            j = i+1
            k = len(nums)-1
            while (j < k):
                if (j == i):
                    j += 1
                    continue
                if (k == i):
                    k -= 1
                    continue
                if (n + nums[j] + nums[k] > 0):
                    k -= 1
                elif (n + nums[j] + nums[k] < 0):
                    j += 1
                else:
                    a = [n, nums[j], nums[k]]
                    if (a not in solutions):
                        solutions.append(a)
                    j += 1
                    k -= 1
        return solutions
