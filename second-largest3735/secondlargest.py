# optimum solution takes 0.31sec..
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

#second solution runs in 0.47sec
class Solution:
    def getSecondLargest(self, arr):
        arr.sort()
        larg = arr[-1]
        larg2 = -1
        for i in arr[-1::-1]:
            if i < larg:
                larg2 = i
                break
        return larg2