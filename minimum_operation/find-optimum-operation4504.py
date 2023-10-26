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

if __name__ == "__main__":
    t = int(input("enter number of tabs : "))
    for i in range(t):
        n = int(input("enter : "))
        ob = Solution()
        print(ob.minOperation(n))