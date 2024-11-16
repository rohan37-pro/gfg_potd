
# this solution takes 0.55sec to run all the samples of gfg
class Solution:
	def pushZerosToEnd(self,arr):
		temp = []
		zero = 0
		for i in arr:
			if i==0:
				zero +=1
			else:
				temp.append(i)
		t = len(temp)
		for i in range(t):
			arr[i] = temp[i]
		for i in range(t, t+zero):
			arr[i] = 0



# this solution exceeds the time limit runs in O(n^2)
class Solution:
	def pushZerosToEnd(self,arr):
		zero = 0
		i = 0
		while i < len(arr):
			if arr[i]==0:
				arr.pop(i)
				zero +=1
			else:
				i+=1
		for i in range(zero):
			arr.append(0)


# this solution runs in 0.61sec.. time complexity O(n) space complexity O(1)
class Solution:
	def pushZerosToEnd(self,arr):
		i = 0
		n = len(arr)
		while i<n and arr[i]!=0:
			i+=1
		j = i
		while i< n and j<n:
			if arr[i]==0:
				while j<n and arr[j]==0:
					j+=1
				if j<n:
					arr[i], arr[j] = arr[j], 0
				i+=1
				

# this solution takes 0.81sec of runtime time complexity O(n)
class Solution:
	def pushZerosToEnd(self,arr):
		ptr = 0
		n = len(arr)
		for i in range(n):
			if arr[i]!=0:
				arr[ptr] = arr[i]
				ptr +=1
		while ptr<n:
			arr[ptr]=0
			ptr+=1