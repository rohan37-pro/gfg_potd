class Solution:
    def minOperation(self, n):
        op = 0
        while n != 0 :
            if n%2==0:
                n //= 2
                op += 1
            else :
                n -= 1
                op += 1
        return op

