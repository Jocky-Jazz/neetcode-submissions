class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        n = l1 + l2
        if (l1==0):
            i = (l2-1)>>1
            return nums2[i] if n%2!=0 else (nums2[i]+nums2[i+1])/2
        if (l2==0):
            i = (l1-1)>>1
            return nums1[i] if n%2!=0 else (nums1[i]+nums1[i+1])/2
        if (len(nums1)>len(nums2)):
            nums1, nums2 = nums2, nums1
            l1, l2 = len(nums1), len(nums2)
        half = l1+((l2-l1+1)>>1)
        for i in range(-1,l1):
            j = half-i-2
            #print(i, j)
            if (i == -1):
                if (nums2[j]<nums1[i+1]):
                    return nums2[j] if n%2!=0 else (nums2[j]+nums1[i+1])/2
                continue
            elif (i == len(nums1)-1):
                return nums1[i] if n%2!=0 else (nums1[i]+nums2[j+1])/2
            elif (nums1[i]<nums2[j+1] and nums2[j]<nums1[i+1]):
                return max(nums1[i], nums2[j]) if n%2!=0 else (max(nums1[i], nums2[j]) + min(nums1[i+1], nums2[j+1]))/2

        return 0
        