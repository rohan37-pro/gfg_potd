'''
	{
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''

class Solution:
    def isPalindrome(self, head):
        pal = []
        while head:
            pal.append(head.data)
            head = head.next
        l = len(pal)//2
        i = 0
        j = -1
        while i<l:
            if pal[i]!= pal[j]:
                return False
            i+=1
            j-=1
        else:
            return True