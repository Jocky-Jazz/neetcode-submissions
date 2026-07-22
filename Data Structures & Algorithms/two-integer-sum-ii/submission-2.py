class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mid = 0
        f = 0
        k = 0
        for x in numbers:
            search = target-x
            l = 0
            u = len(numbers)-1
            while (l <= u):
                mid = (l+u)//2
                if (search == numbers[mid]):
                    f=1
                    break
                elif (search < numbers[mid]):
                    u = mid-1
                else:
                    l = mid+1
            if (f==1 and not (mid == k)):
                return [k+1, mid+1]
            k = k+1
