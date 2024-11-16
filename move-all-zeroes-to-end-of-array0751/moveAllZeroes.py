
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
