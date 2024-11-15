class Solution:
    def getSecondLargest(self, arr):
        second = -1
        large = arr[0]
        for i in arr[1:]:
            if i>large:
                second = large
                large = i
            elif i>second and i!=large:
                second = i
        return second
