
class Solution:
    def maxStep(self, arr):
        maximum = 0
        Current = 0
        elem = arr[0]
        for i in arr[1:]:
            if i>elem:
                Current+=1
                if Current> maximum:
                    maximum = Current
            else:
                Current = 0
            elem = i
        return maximum
        