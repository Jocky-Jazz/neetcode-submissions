class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)+len(nums2)
        if (len(nums1)==0):
            i = (len(nums2)-1)>>1
            return nums2[i] if n%2!=0 else (nums2[i]+nums2[i+1])/2
        if (len(nums2)==0):
            i = (len(nums1)-1)>>1
            return nums1[i] if n%2!=0 else (nums1[i]+nums1[i+1])/2
        if (len(nums1)>len(nums2)):
            nums1, nums2 = nums2, nums1
        half = len(nums1)+((len(nums2)-len(nums1)+1)>>1)
        for i in range(-1,len(nums1)):
            j = half-i-2
            #print(i, j)
            if (i == -1):
                if (nums2[j]<nums1[i+1]):
                    return nums2[j] if n%2!=0 else (nums2[j]+nums1[i+1])/2
                continue
            elif (i == len(nums1)-1):
                return nums1[i] if n%2!=0 else (nums1[i]+nums2[j+1])/2
            elif (nums1[i]<nums2[j+1] and nums2[j]<nums1[i+1]):
                a = max(nums1[i], nums2[j]) 
                return a if n%2!=0 else (a + min(nums1[i+1], nums2[j+1]))/2

        return 0
        