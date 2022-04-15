class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data,"->",end=" ")
            printval = printval.next
        
    def AtStart(self,data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def AtEnd(self,data):
        new = Node(data)
        if self.head is not None:
            self.head = new
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new



if __name__=='__main__':
    list = LinkedList()
    list.head = Node(56)
    n1 = Node(45)
    n2 = Node(89)

    list.head.next = n1
    n1.next = n2

    list.listprint()
    print()
    list.AtStart(12)
    list.listprint()
    list.AtEnd(99)
    list.listprint()


