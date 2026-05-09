class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_head (self, value):
        new_node = Node (value)
        new_node.next = self.head
        self.head = new_node

    def traverse (self):
        cur = self.head
        while(cur != None):
            print (cur.value)
            cur = cur.next

linkedlist = LinkedList()
linkedlist.insert_head(5)
linkedlist.insert_head(6)
linkedlist.insert_head(7)
linkedlist.insert_head(9)

linkedlist.traverse()