class Solution:
    def editDistance(self, str1, str3):
        operations = 0
        found = 0
        next = 0
        startAtIndex = 0
        EndAtIndex=None
        for s3 in str3:
            for s1 in range(next, len(str1)):
                if str1[s1] == s3:
                    next=s1+1
                    # print("found ",s3,"next=",next,end=" ")
                    found += 1
                    if found ==1:
                        startAtIndex = s1
                    else :
                        EndAtIndex = s1
                    break
        # print()
        s1_len =EndAtIndex - startAtIndex + 1
        # print(f"length str1={str1}, str3={str3}")
        # print("s1_len=", s1_len)
        # print(f"found = {found}")
        operations += len(str1) - s1_len
        if len(str3) < s1_len:
            operations +=  s1_len - len(str3)
            operations += len(str3) - found
        elif len(str3) >= s1_len:
            operations += len(str3) - found
        return operations
    

str1 = input("enter str1 : ")
str3 = input("enter str2 : ")

obj = Solution()
print(obj.editDistance(str1, str3))