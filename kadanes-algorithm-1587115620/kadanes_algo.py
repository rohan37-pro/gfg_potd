class Solution:
    def maxSubArraySum(self,arr):
        cur =0
        maxtillnow = -10000009
        for i in arr:
            cur += i
            maxtillnow = max(maxtillnow, cur)
            if cur < 0 :
                cur = 0
        return maxtillnow