# this easiest solution is taking too much time. time complexity O(d*n) longer then 2.07
class Solution:
    def rotateArr(self, arr, d):
        d = d%len(arr) 
        for i in range(d):
            a = arr.pop(0)
            arr.append(a)


# this solution takes 0.56sec to run time complexity O(2d+n)
class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d%n
        temp = []
        for i in range(d):
            temp.append(arr[i])
        for i in range(n-d):
            arr[i] = arr[i+d]
        j = n-d
        for i in temp:
            arr[j] = i
            j+=1
        