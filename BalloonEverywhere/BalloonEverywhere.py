

class Solution:
	def maxInstance(self, s ) :
		ballon = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
		for i in s:
			if i in "balon":
				ballon[i] += 1

		ballon['l'] //= 2
		ballon['o'] //=2
		lis_ballon = []
		for i in ballon:
			lis_ballon.append(ballon[i])
		
		lis_ballon.sort()
		return lis_ballon[0]


s = input("enter string : ")

obj = Solution()
res = obj.maxInstance(s)
print(res)