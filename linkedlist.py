from node import Node
class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    
    def popfirst(self):
        if self.head == None:
            return
        self.head = (self.head).next
    
    def peek(self):
        if self.head != None:
            return self.head.data 

    def displayboard(self):
        orders = ""
        current = self.head
        while current.next:
            orders = orders + ", " + str(current.data)
            current = current.next
        orders = orders + ", " + str(current.data)
        return orders