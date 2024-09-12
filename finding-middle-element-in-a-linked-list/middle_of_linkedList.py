

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def getMiddle(self, head):
        cur = head
        size = 0
        while cur:
            cur = cur.next
            size += 1
        middle = size//2 + 1
        cur = head
        while middle>1:
            cur = cur.next
            middle-=1
        return cur.data

head_list = [1,2,3,4,5,6,7,8,9,10,11,12]
head = node(head_list[0])
cur = head
for i in head_list[1:]:
    cur.next = node(i)
    cur = cur.next

obj = Solution()
print(obj.getMiddle(head))