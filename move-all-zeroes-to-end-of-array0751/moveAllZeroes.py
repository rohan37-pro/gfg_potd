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
		for i in temp