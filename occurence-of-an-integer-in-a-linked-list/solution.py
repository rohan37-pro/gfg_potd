class Solution:
    def count(self, head, key):
        c = 0
        while head:
            if head.data == key:
                c+=1
            head = head.next
        return c