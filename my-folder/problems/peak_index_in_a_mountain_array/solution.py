class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        while l<=r:
            mid =(l+r)//2
            if (mid == 0 or arr[mid]>=arr[mid-1]) and (mid == len(arr)-1 or arr[mid]>=arr[mid+1]):
                return mid
            elif mid>0 and arr[mid-1]>arr[mid]:
                r = mid-1
            else:
                l = mid+1