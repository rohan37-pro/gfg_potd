# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def multiply_two_lists(self, first, second):
        mod = 1000000007
        num1 = ''
        while first:
            num1 += str(first.data)
            first = first.next
            num1 = str(int(num1)%mod)
        num2 = ''
        while second:
            num2 += str(second.data)
            second = second.next
            num2 = str(int(num2)%mod)
        
        return (int(num1) * int(num2)) % mod
