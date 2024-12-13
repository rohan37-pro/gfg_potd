class Solution:
    def findMin(self, arr):
        small = arr[0]
        j = 0
        for i in range(1, len(arr)):
            if arr[j]>arr[i]:
                small = arr[i]
                break
        return small
