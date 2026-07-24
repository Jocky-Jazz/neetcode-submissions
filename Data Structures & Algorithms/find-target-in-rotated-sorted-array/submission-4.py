class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, u = 0, len(nums)-1
        minim = 0
        while (l < u):
            minim= l+((u-l)>>1)
            if (nums[minim] < nums[u]):
                u = minim
            else:
                l = minim+1
        minim = l
        if (target > nums[-1]):
            u = minim-1
            l = 0
        else:
            u = len(nums)-1
            l = minim
        print(l, u)
        while (l <= u):
            mid = l + ((u-l)>>1)
            if (nums[mid]<target):
                l = mid+1
            elif (nums[mid]>target):
                u = mid-1
            else:
                return mid
        return -1
                
