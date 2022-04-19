from requests import delete, head


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
        if self.head is None:
            self.head = new
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new

    def Inbetween(self,middlenode,data):
        new = Node(data)
        if middlenode is None:
            print("The provided node is missing")
            return
        new.next = middlenode.next
        middlenode.next = new

    def delete(self,key):
        headpoint  = self.head

        if headpoint is not None:
            if headpoint.data == key:
                self.head =headpoint.next
                headpoint = None
                return
        while headpoint is not None:
            if headpoint.data == key:
                break
            prev = headpoint
            headpoint = headpoint.next

        if headpoint == None:
            return
        prev.next = headpoint.next
        headpoint = None



if __name__=='__main__':
    list = LinkedList()
    list.head = Node(56)
    n1 = Node(45)
    n2 = Node(89)

    list.listprint()

    list.head.next = n1
    n1.next = n2
    print()
    list.listprint()
    print()
    list.AtStart(12)
    list.listprint()
    print()
    list.AtEnd(99)
    list.listprint()
    print()
    list.Inbetween(list.head,100)
    list.listprint()

    print()
    list.delete(100)
    list.listprint()


