class Solution:
    def findTriplet(self, arr):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i]+arr[j] in arr:
                    return True
        return False
