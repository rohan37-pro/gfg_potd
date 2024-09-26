#User function Template for python3
class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        maximum = 0
        Current = 0
        elem = arr[0]
        for i in arr[1:]:
            if i>elem:
                Current+=1
                maximum = max(maximum, Current)
            else:
                Current = 0
            elem = i
        return maximum