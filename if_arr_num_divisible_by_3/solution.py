class Solution:
    def isPossible(self, N, arr):
        mod = 0
        for i in arr:
            mod += i % 3
        if mod%3==0:
            return 1
        else :
            return 0
