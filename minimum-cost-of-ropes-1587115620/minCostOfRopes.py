import heapq

class Solution:
   def minCost(self, arr) :
        heapq.heapify(arr)
        cost = 0
        while len(arr)>1:
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            cost += first+second
            heapq.heappush(arr, first+second)
            
        return cost
    
obj = Solution()
print(obj.minCost([4, 2, 7, 6, 9]))
