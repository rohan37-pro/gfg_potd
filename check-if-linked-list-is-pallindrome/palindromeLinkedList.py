
'''
	Your task is to check if given linkedlist
	is a pallindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

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