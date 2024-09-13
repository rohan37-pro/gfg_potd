class Solution:
    def findNth(self,n):
        nth = ""
        while n:
            remainder = n%9
            nth = str(remainder) + nth
            n = n//9
        return nth

obj = Solution()
print(obj.findNth(10))