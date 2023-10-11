

class Solution:
    def sortedInsert(self, head1,key):
        current = head1
        added = 0
        
        if current.data:
            if current.data > key:
                new_node = Node(key)
                new_node.next = current
                added = 1
                return new_node
            
            while current.next:
                if current.next.data > key:
                    new_node = Node(key)
                    new_node.next = current.next
                    current.next = new_node
                    added = 1
                    break
                else:
                   current = current.next
            if added == 0 :
                new_node = Node(key)
                current.next = new_node
                    
                    
        else :
            head1.data = key
            head1.next = None
            
        return head1
