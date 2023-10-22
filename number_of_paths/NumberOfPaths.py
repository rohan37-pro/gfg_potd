class Solution:
    def numberOfPaths (self, M, N):
        M -= 1
        N -= 1
        r = min(M, N)
        N = M + N
        mod = 10**9 +7
        def factorial(s, f):
            fact = 1
            for i in range(s, f+1):
                fact *= i 
            return fact
        
        path = factorial(N-r+1 , N)// factorial(1, r)
        return path % mod


if __name__ == "__main__" :
    ob = Solution()
    t = int(input())
    for _ in range(t) :
        m , n = map(int, input().split())
        ans = ob.numberOfPaths(m, n)
        print(ans)