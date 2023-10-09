

class Solution:
	def inSequence(self, A, B, C):
		if C == 0 and A != B:
			return 0
		elif C == 0 and A == B:
			return 1

		if B < A and C > 0:
			return 0
		elif B > A and C < 0:
			return 0
			
		if (B - A)%C == 0:
			return 1
		else :
			return 0







if __name__ == "__main__":
	a, b, c = [int(x) for x in input("enter : ").split()]

	obj = Solution()
	print(obj.inSequence(a,b,c))