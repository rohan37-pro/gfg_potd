#User function Template for python3

class Solution:
    def totalCount(self, k, arr):
        sum = 0
        for i in arr:
            sum += (i//k)
            if i%k!=0:
                sum+=1
        return sum
        