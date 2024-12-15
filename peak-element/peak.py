class Solution:   
    def peakElement(self,arr):
        n = len(arr)
        if n==0:
            return None
        if n==1 or arr[0]>arr[1]:
            return 0
        if arr[-1]>arr[-2]:
            return n-1
        for i in range(1,n-1):
            if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                return i
        return None