class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        counter012 = {0:0, 1:0, 2:0}
        for i in arr:
            counter012[i] += 1
        for i in range(counter012[0]):
            arr[i] = 0
        for i in range(counter012[0], counter012[0]+counter012[1]):
            arr[i] = 1
        for i in range(-1, - counter012[2]-1, -1):
            arr[i] = 2
            
# arr = [0, 2, 1, 2, 0]

# obj = Solution()
# obj.sort012(arr)
# print(arr)