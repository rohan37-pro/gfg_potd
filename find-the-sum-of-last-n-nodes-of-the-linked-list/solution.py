class Solution:
    def sumOfLastN_Nodes(self, head, n):
        cur = head
        nodes = 0
        while cur:
            nodes+=1
            cur = cur.next
        cur = head
        for i in range(nodes-n):
            cur = cur.next
        sum = 0
        while cur:
            sum += cur.data
            cur = cur.next
        return sum