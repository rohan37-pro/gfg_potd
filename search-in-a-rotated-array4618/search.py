class Solution:
    def search(self,arr,key):
        n = len(arr)
        if key>=arr[0]:
            for i in range(n):
                if arr[i]==key:
                    return i
                if arr[i]>key:
                    return -1
                if i+1<n and arr[i+1]<arr[i]:
                    return -1
                
        if key<arr[0]:
            for i in range(-1, -n-1, -1):
                if arr[i]==key:
                    return n+i
                if arr[i]<key:
                    return -1
                if i-1>=0 and arr[i-1]>arr[i]:
                    return -1
        return -1