class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)+len(nums2)
        if (len(nums1)==0):
            i = (len(nums2)-1)>>1
            return nums2[i] if n%2!=0 else (nums2[i]+nums2[i+1])/2
        if (len(nums2)==0):
            i = (len(nums1)-1)>>1
            return nums1[i] if n%2!=0 else (nums1[i]+nums1[i+1])/2
        n1, n2= [], []
        if (len(nums1)<len(nums2)):
            n1=nums1
            n2=nums2
        else:
            n1=nums2
            n2=nums1
        half = len(nums1)+((len(nums2)-len(nums1)+1)>>1)
        for i in range(-1,len(n1)):
            j = half-i-2
            #print(i, j)
            if (i == -1):
                if (n2[j]<n1[i+1]):
                    return n2[j] if n%2!=0 else (n2[j]+n1[i+1])/2
                continue
            elif (i == len(n1)-1):
                return n1[i] if n%2!=0 else (n1[i]+n2[j+1])/2
            elif (n1[i]<n2[j+1] and n2[j]<n1[i+1]):
                a = max(n1[i], n2[j]) 
                return a if n%2!=0 else (a + min(n1[i+1], n2[j+1]))/2

        return 0
        