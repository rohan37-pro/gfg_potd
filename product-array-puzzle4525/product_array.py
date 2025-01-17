
class Solution:
    def productExceptSelf(self, arr):
        product = 1
        zero_count = 0
        for i in arr:
            if i==0:
                zero_count+=1
            else:
                product*=i
        if zero_count>1:
            return [0]*len(arr)
        if zero_count==1:
            ind = arr.index(0)
            array = [0]*len(arr)
            array[ind]=product
            return array
        
        for i in range(len(arr)):
            arr[i] = product//arr[i]
        return arr

arr = [12,0]
print(Solution().productExceptSelf(arr))