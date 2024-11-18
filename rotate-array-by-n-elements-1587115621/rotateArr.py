class Solution:
    def rotateArr(self, arr, d):
        for i in range(d):
            a = arr.pop(0)
            arr.append(a)
    