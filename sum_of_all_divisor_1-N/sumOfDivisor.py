
class Solution:
    def sumOfDivisors(self, N):
        sum = 0
        for i in range(1, N+1):
            print(f"for intager {i} :")
            for j in range(1, int(i**0.5)+1):
                print(f"{j}", end="")
                if i%j==0:
                    sum += j
                    print(f"<- ", end="")
                    if j != (i//j):
                        sum += i//j
                        print(f"{i//j}<- ", end="")
            print()
        return sum

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)