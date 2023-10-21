
class Solution:
    def sumOfDivisors(self, N):
        sum = 0
        for i in range(1, N+1):
            for j in range(1, int(i**0.5)+1):
                if i%j==0:
                    sum += j
                    if j != (i//j):
                        sum += i//j
        return sum


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)